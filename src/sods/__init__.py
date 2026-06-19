"""
SODS (Sandbox Observer-Driven Specializer) Package
==================================================
A conceptual runtime specialization wrapper demonstrating runtime profile observation,
Polymorphic Inline Caches (PIC), empirical equivalence verification, OSR deoptimization,
tier-lowering on highly volatile call sites, and side-effect taint checking.

Copyright (c) 2026 Fajar Kurnia
Licensed under MIT or Apache-2.0.
"""

from .profile import Profile
from .specializer import make_specialized_add
from .verifier import EquivalenceVerifier
from .sandbox import SODSSandbox

__all__ = [
    "Profile",
    "make_specialized_add",
    "EquivalenceVerifier",
    "SODSSandbox",
]
