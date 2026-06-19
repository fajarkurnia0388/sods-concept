"""
Specializer Builder Component
=============================
Generates specialized dynamic fast paths wrapped in a 'SpecializedFunction' class.
Tracks Guard failures synchronously. When inputs deviate from the observed PIC table,
the Guard increments its internal deopt counter and evacuates execution (OSR) back
to the safe generic target.
"""

from typing import Tuple, Callable, Any, List

class SpecializedFunction:
    def __init__(self, allowed_types: Tuple[Tuple[type, type], ...], generic_fn: Callable, label: str, supported_sigs: List[Tuple[str, str]]):
        self.allowed_types = allowed_types
        self.generic_fn = generic_fn
        self.label = label
        self.supported_sigs = supported_sigs
        self.deopt_count = 0

    def __call__(self, a: Any, b: Any) -> Any:
        # ── GUARD INSPECTION ENTRY BOUNDARY ─────────────────────────────────
        # In Machine Code: `cmp type(a), expected_type / jne _deopt_evacuation`
        # Tracks Guard failures 100% synchronously.
        # ────────────────────────────────────────────────────────────────────
        if (type(a), type(b)) not in self.allowed_types:
            self.deopt_count += 1
            return self.generic_fn(a, b)
            
        # Raw Instruction Execution — bypassing high-level dictionary lookup overheads
        return a + b

def make_specialized_add(stable_signatures: List[Tuple[str, str]], generic_fn: Callable) -> Tuple[Callable, str, List[Tuple[str, str]]]:
    """
    Builds a 'SpecializedFunction' callable object for the observed stable type signatures.
    Filters signatures to ensure only supported combinations form the PIC.
    """
    type_map = {
        ("int", "int"): (int, int),
        ("float", "float"): (float, float),
        ("str", "str"): (str, str),
        ("list", "list"): (list, list),
        ("int", "float"): (int, float),
        ("float", "int"): (float, int),
    }
    
    # Filter stable signatures to include only those supported by our JIT emitter
    supported_signatures = [
        sig for sig in stable_signatures if sig in type_map
    ]
    
    allowed_types = tuple(type_map[sig] for sig in supported_signatures)

    if not allowed_types:
        # Fallback if none of the observed stable signatures are supported
        return generic_fn, "Generic Passthrough (no supported PIC signatures)", []

    pic_label = f"Polymorphic Inline Cache (PIC: {len(supported_signatures)})"
    spec_obj = SpecializedFunction(allowed_types, generic_fn, pic_label, supported_signatures)
    
    return spec_obj, pic_label, supported_signatures
