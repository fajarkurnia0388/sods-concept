"""
Dummy Application Target Implementations
========================================
Simulates bloated/dynamic generic application workloads that handle multiple data
types with heavy type-dispatch lookup and boxing overheads.
"""

DISPATCH_TABLE = {
    ("int", "int"): "i_add",
    ("float", "float"): "f_add",
    ("str", "str"): "s_concat",
    ("list", "list"): "l_extend",
    ("int", "float"): "mixed_numeric",
    ("float", "int"): "mixed_numeric",
}

def generic_add(a, b):
    """
    Generic polymorphic add function: handles int, float, str, list, and mixed numerics.
    Intentionally bloated with type-dispatch table lookup and string representation
    overhead to simulate dynamic language runtime dispatch (like JS or Python).
    """
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("bool is not supported")

    ta, tb = type(a).__name__, type(b).__name__
    entry = DISPATCH_TABLE.get((ta, tb))
    
    # Simulate lookup/boxing penalty
    _ = entry.__repr__() if entry else ""

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    if isinstance(a, list) and isinstance(b, list):
        return a + b
    raise TypeError(f"Unsupported types: {ta} + {tb}")

def generic_log_io(message):
    """
    Function with side-effects (Side-Effect I/O boundary).
    Simulates logging to disk or communicating across a network.
    """
    _ = f"[SYSCALL I/O] {message}"
    return True
