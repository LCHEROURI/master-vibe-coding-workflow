#!/usr/bin/env bash
# A separate observable workflow; all data is synthetic and disposable.
set -euo pipefail
cd -- "$(dirname -- "$0")"
demo_dir=$(mktemp -d)
trap 'rm -rf -- "$demo_dir"' EXIT
db="$demo_dir/tasks.sqlite3"

# Trace actual commands, including temporary paths, into captured evidence.
set -x
python3 tasks.py --db "$db" list > "$demo_dir/empty.json"
cat "$demo_dir/empty.json"
python3 tasks.py --db "$db" add "Read WORKFLOW.md"
python3 tasks.py --db "$db" add "Record evidence"
python3 tasks.py --db "$db" done 1
python3 tasks.py --db "$db" list > "$demo_dir/before.json"
cat "$demo_dir/before.json"

# Each CLI process has exited: this is an offline backup, never a live copy.
cp "$db" "$demo_dir/backup.sqlite3"
python3 tasks.py --db "$db" add "Temporary task"
python3 tasks.py --db "$db" list > "$demo_dir/modified.json"
cat "$demo_dir/modified.json"
cp "$demo_dir/backup.sqlite3" "$db"
python3 tasks.py --db "$db" list > "$demo_dir/restored.json"
cat "$demo_dir/restored.json"
cmp "$demo_dir/before.json" "$demo_dir/restored.json"
python3 - "$demo_dir" <<'PY'
import json
from pathlib import Path
import sys

root = Path(sys.argv[1])
assert json.loads((root / "empty.json").read_text()) == []
expected = [
    {"id": 1, "title": "Read WORKFLOW.md", "done": True},
    {"id": 2, "title": "Record evidence", "done": False},
]
assert json.loads((root / "before.json").read_text()) == expected
assert json.loads((root / "modified.json").read_text()) == expected + [
    {"id": 3, "title": "Temporary task", "done": False},
]
assert json.loads((root / "restored.json").read_text()) == expected
print("PASS: CLI lifecycle and offline restore match expected task data")
PY
