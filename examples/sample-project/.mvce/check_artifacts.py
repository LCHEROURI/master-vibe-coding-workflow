"""Check evidence freshness, local document links, and this change's path scope."""

import hashlib
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote


SAMPLE = Path(__file__).resolve().parents[1]
ROOT = SAMPLE.parents[1]
BASE = "ea023e27bdec1b08cad74b7660f9a94288cf52c0"


def check():
    artifacts = [SAMPLE / "PROJECT-SPEC.md"] + [
        SAMPLE / ".mvce" / (name + ".md")
        for name in [
            "WORKBOOK", "AUTHORITY-LEASE", "BUILD-PLAN", "ACCEPTANCE-CRITERIA",
            "RISK-REGISTER", "VERIFICATION", "EVIDENCE-LEDGER",
            "DEPLOYMENT-CHECKLIST", "RECOVERY-PLAN",
        ]
    ]
    for path in artifacts:
        assert path.is_file() and path.read_text().strip(), path
    print(f"PASS: {len(artifacts)} required completed-artifact files exist (content requires review)")

    links = 0
    for path in SAMPLE.rglob("*.md"):
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
            if re.match(r"^[a-zA-Z]+:", target) or target.startswith("#"):
                continue
            destination = unquote(target.split("#")[0])
            assert (path.parent / destination).exists(), (path, target)
            links += 1
    print(f"PASS: {links} local Markdown link destinations exist (anchors not checked)")

    for log in ["02-green-tests.txt", "03-cli-and-recovery.txt"]:
        content = (SAMPLE / ".mvce/evidence" / log).read_text()
        assert "--- exit status: 0 ---" in content, log
        for name in ["tasks.py", "tests/test_tasks.py", "smoke.sh"]:
            digest = hashlib.sha256((SAMPLE / name).read_bytes()).hexdigest()
            assert f"SHA256 {name}: {digest}" in content, (log, name)
    print("PASS: green/smoke evidence hashes match current app, tests, and smoke script")

    changed = subprocess.check_output(
        ["git", "diff", "--name-only", BASE], cwd=ROOT, text=True,
    ).splitlines()
    untracked = subprocess.check_output(
        ["git", "ls-files", "--others", "--exclude-standard"], cwd=ROOT, text=True,
    ).splitlines()
    for name in set(changed + untracked):
        assert name == "README.md" or name.startswith("examples/sample-project/"), name
    print("PASS: changed/untracked paths are inside sample or root README")
    subprocess.run(["git", "diff", "--check", BASE], cwd=ROOT, check=True)
    print("PASS: git diff --check against baseline")


if __name__ == "__main__":
    check()
