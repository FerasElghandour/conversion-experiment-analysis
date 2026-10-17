"""Offline example using the public implementation; see README for evidence scope."""
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
os.chdir(ROOT)

from experiment import compare
# Retained sufficient counts, with an explicit 500-draw simulation budget.
result = compare(3650, 34678, 5469, 35211, draws=500, seed=42)

import json
print(json.dumps(result, indent=2))

