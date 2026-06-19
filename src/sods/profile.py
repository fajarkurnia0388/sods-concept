"""
Observer & Profiler Component
=============================
Responsible for recording call signatures and extracting stable signatures
for Polymorphic Inline Caches (PIC) during the cold execution run.
"""

class Profile:
    def __init__(self, hot_threshold: int = 50):
        self.type_seen = {}       # fn_name -> {type_signature_tuple: count}
        self.call_count = {}      # fn_name -> total calls
        self.hot_threshold = hot_threshold

    def record(self, fn_name: str, args: tuple) -> None:
        self.call_count[fn_name] = self.call_count.get(fn_name, 0) + 1
        types = tuple(type(a).__name__ for a in args)
        bucket = self.type_seen.setdefault(fn_name, {})
        bucket[types] = bucket.get(types, 0) + 1

    def get_stable_signatures(self, fn_name: str) -> list:
        """
        Extracts up to 3 stable signatures for Polymorphic Inline Caching (PIC).
        Only includes type signatures that account for at least 15% of total calls.

        [PRODUCTION NOTE — Chapter 5.6.3]
        In production systems, this profile metadata is populated asynchronously via
        Hardware PMU Statistical Sampling (Linux perf), imposing < 1% CPU overhead.
        """
        if fn_name not in self.type_seen:
            return []
        bucket = self.type_seen[fn_name]
        total = sum(bucket.values())
        
        # Sort signatures by frequency descending
        sorted_types = sorted(bucket.items(), key=lambda x: x[1], reverse=True)
        
        stable = []
        for t_sig, count in sorted_types:
            if count / total > 0.15:
                stable.append(t_sig)
                if len(stable) == 3:  # PIC capacity capped at 3 observed types
                    break
        return stable

    def is_hot(self, fn_name: str) -> bool:
        return self.call_count.get(fn_name, 0) >= self.hot_threshold
