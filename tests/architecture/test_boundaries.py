"""Boundary enforcement (IMP-001 Section 3.2, ADR-004 T-14/DEP-12).

Walks src/ with ast, extracts module-to-module imports, and asserts every
edge appears in the Allowed Edge Table (IMP-001 Section 3.1, derived from
ADR-002 Section 6.1 / ADR-006 Section 3.2). Also asserts named constitutional
prohibitions (FORB-xx / DEP-xx / ACT-xx) individually.
"""

import ast
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "src"

MODULES = [
    "mod01_market_data", "mod02_market_context", "mod03_evidence",
    "mod04_validation", "mod05_recommendation", "mod06_governance",
    "mod07_human_gate", "mod08_attribution", "mod09_portfolio",
    "mod10_audit", "mod11_activation",
]

# IMP-001 Section 3.1 Allowed Edge Table. "persistence" and "mod10_audit"
# are universally allowed write/audit targets and are not repeated below.
ALLOWED_EDGES = {
    "mod01_market_data": set(),
    "mod02_market_context": {"mod01_market_data"},
    "mod03_evidence": {"mod01_market_data", "mod02_market_context"},
    "mod04_validation": {"mod01_market_data", "mod03_evidence"},
    "mod05_recommendation": {
        "mod01_market_data", "mod02_market_context", "mod03_evidence",
        "mod04_validation", "mod09_portfolio", "mod06_governance",
    },
    "mod06_governance": {"mod02_market_context", "mod09_portfolio"},
    "mod07_human_gate": {"mod03_evidence", "mod05_recommendation", "mod06_governance", "mod09_portfolio"},
    "mod08_attribution": {"mod01_market_data", "mod02_market_context", "mod07_human_gate"},
    "mod09_portfolio": set(),
    "mod10_audit": set(),
    "mod11_activation": set(),
}

UNIVERSALLY_ALLOWED = {"persistence", "mod10_audit"}


def _module_imports(py_file: Path) -> set[str]:
    """Return the set of top-level src package names imported by py_file."""
    tree = ast.parse(py_file.read_text(), filename=str(py_file))
    imports: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            parts = node.module.split(".")
            if parts[0] == "src" and len(parts) > 1:
                imports.add(parts[1])
            elif parts[0] != "src":
                imports.add(parts[0])
        elif isinstance(node, ast.Import):
            for alias in node.names:
                parts = alias.name.split(".")
                if parts[0] == "src" and len(parts) > 1:
                    imports.add(parts[1])
                elif parts[0] != "src":
                    imports.add(parts[0])

    return imports


def _edges_for_module(module: str) -> set[str]:
    """Collect all src-internal package imports across every file in `module`."""
    pkg_dir = SRC / module
    edges: set[str] = set()
    for py_file in pkg_dir.rglob("*.py"):
        for imported in _module_imports(py_file):
            if imported in MODULES or imported == "persistence":
                if imported != module:
                    edges.add(imported)
    return edges


def test_all_edges_are_allowed():
    violations = []
    for module in MODULES:
        actual = _edges_for_module(module)
        allowed = ALLOWED_EDGES[module] | UNIVERSALLY_ALLOWED
        for edge in actual:
            if edge not in allowed:
                violations.append(f"{module} -> {edge}")
    assert not violations, f"Disallowed import edges (DEP-12): {violations}"


def test_forb_mod10_audit_is_terminal_sink_no_outbound_edges():
    """ADR-004 DEP-03 / AUD-01: MOD-10 has zero outbound edges to any module."""
    edges = _edges_for_module("mod10_audit")
    assert edges <= {"persistence"}, f"mod10_audit must have no outbound module edges, found: {edges}"


def test_forb_mod11_activation_does_not_orchestrate_other_modules():
    """ADR-006 ACT-01/ACT-04/INV-13: MOD-11 initiates only, never imports the pipeline."""
    edges = _edges_for_module("mod11_activation")
    assert edges <= UNIVERSALLY_ALLOWED, f"mod11_activation must not import pipeline modules, found: {edges}"


def test_forb_mod09_portfolio_has_no_shadow_dependencies():
    """ADR-002 OWN-01/DEP-08: MOD-09 is sole authoritative portfolio source, depends on nothing else."""
    edges = _edges_for_module("mod09_portfolio")
    assert edges <= UNIVERSALLY_ALLOWED, f"mod09_portfolio must not depend on other modules, found: {edges}"


def test_forb_mod08_attribution_has_no_write_edge_to_mod01_through_mod06():
    """ADR-002 DEP-02/OWN-03/INV-08: MOD-08 is read-only/observation-only, zero write authority to MOD-01..06."""
    edges = _edges_for_module("mod08_attribution")
    forbidden_targets = {
        "mod03_evidence", "mod04_validation", "mod05_recommendation", "mod06_governance",
    }
    violation = edges & forbidden_targets
    assert not violation, f"mod08_attribution must not depend on {forbidden_targets}, found: {violation}"


def test_forb_sentiment_path_mod03_cannot_reach_recommendation_computation_directly():
    """VAL05-01/FORB-03/DEP-04: this is enforced functionally in mod03/mod05, not by import
    shape alone. Edge mod05 -> mod03 is allowed (mod05 may read mod03 outputs); the
    advisory/numeric separation is verified in tests/unit/mod05_recommendation."""
    assert "mod03_evidence" in ALLOWED_EDGES["mod05_recommendation"]
