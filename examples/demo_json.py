import sys
import os

# Add the src directory to PYTHONPATH so we can import sods
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from sods.sandbox import SODSSandbox
import json

def generic_json_parse(json_string):
    """
    A generic JSON parser that can accept any string.
    In real-world applications, this represents a target function we want to optimize.
    """
    return json.loads(json_string)

def main():
    print("=" * 72)
    print(" 🚀 SODS DEMO: JSON PARSING".center(72))
    print("=" * 72)
    
    sandbox = SODSSandbox()
    
    print("\n[Tahap 1] Melakukan observasi (Cold Run)...")
    workload = ['{"key": "value", "number": 1}', '{"message": "hello world"}'] * 10
    
    for item in workload:
        sandbox.cold_run(generic_json_parse, item)
        
    print("\n[Tahap 2] Membangkitkan Biner Terspesialisasi...")
    # SODS will create a specialized fast path based on the observed data
    sandbox.specialize(generic_json_parse)
    
    print("\n[Tahap 3] Eksekusi Cepat (Warm Run)...")
    # Now we execute the fast path
    print(" Mengurai: '{\"status\": \"success\"}'")
    result = sandbox.warm_run(generic_json_parse, '{"status": "success"}')
    print(f" Hasil    : {result}")
    
    print("\n[Tahap 4] Menguji Deoptimisasi (Fallback)...")
    # What if we pass something unexpected?
    print(" Mengurai: '[\"unexpected\", \"array\"]'")
    result = sandbox.warm_run(generic_json_parse, '["unexpected", "array"]')
    print(f" Hasil    : {result} (Dieksekusi via fallback karena guard gagal)")
    
    print("\n✨ Demo Selesai. Profile tersimpan di direktori .sods/")

if __name__ == "__main__":
    main()
