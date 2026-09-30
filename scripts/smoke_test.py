"""Setup check. Run in the terminal:  python scripts/smoke_test.py

Prints one line per check and a final SETUP VERIFIED line. Screenshot that line.
"""
import importlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

ok = True
print(f"Python {sys.version.split()[0]}")

for module in ("pandas", "plotly", "dash", "openpyxl", "pyarrow", "boto3", "docx"):
    try:
        importlib.import_module(module)
        print(f"  {module:10} ok")
    except ImportError:
        print(f"  {module:10} MISSING")
        ok = False

if shutil.which("claude"):
    version = subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip()
    print(f"  {'claude':10} {version}")
else:
    print(f"  {'claude':10} MISSING")
    ok = False

key_ok = os.environ.get("ANTHROPIC_API_KEY", "").startswith("sk-ant-")
print(f"  {'class key':10} {'found' if key_ok else 'MISSING - see README, step 2'}")
ok = ok and key_ok

data = Path(__file__).resolve().parent.parent / "data" / "monthlysummary.csv"
if data.exists():
    rows = sum(1 for _ in data.open(encoding="utf-8")) - 1
    print(f"  {'data':10} {rows:,} flight rows")
else:
    print(f"  {'data':10} MISSING")
    ok = False

print()
print("SETUP VERIFIED - screenshot this line" if ok else "SETUP INCOMPLETE - ask an instructor")
sys.exit(0 if ok else 1)
