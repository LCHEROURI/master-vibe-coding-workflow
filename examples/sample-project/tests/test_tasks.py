"""Acceptance tests against the real CLI, real files, and fresh processes."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1] / "tasks.py"


class TasksCLI(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db = Path(self.temp.name) / "tasks.sqlite3"

    def command(self, *args, status=0, db=None):
        result = subprocess.run(
            [sys.executable, str(APP), "--db", str(db or self.db), *args],
            capture_output=True, text=True, encoding="utf-8", timeout=10,
        )
        self.assertEqual(result.returncode, status, result.stderr)
        if status:
            self.assertEqual(result.stdout, "")
            self.assertIn("error:", result.stderr)
            self.assertNotIn("Traceback", result.stderr)
            return result
        self.assertEqual(result.stderr, "")
        return json.loads(result.stdout)

    def test_empty_then_add_persists_ac1(self):
        self.assertEqual(self.command("list"), [])
        task = self.command("add", "Read the workflow")
        self.assertIs(type(task["id"]), int)
        self.assertGreater(task["id"], 0)
        self.assertEqual(task["title"], "Read the workflow")
        self.assertIs(task["done"], False)
        self.assertEqual(self.command("list"), [task])

    def test_literal_titles_and_order_ac2(self):
        first = self.command("add", "  café ☕  ")
        second = self.command("add", "Robert'); DROP TABLE tasks;--")
        self.assertEqual(first["title"], "café ☕")
        self.assertEqual(second["title"], "Robert'); DROP TABLE tasks;--")
        self.assertGreater(second["id"], first["id"])
        self.assertEqual(self.command("list"), [first, second])

    def test_complete_one_idempotently_ac3(self):
        first = self.command("add", "First")
        second = self.command("add", "Second")
        expected = dict(first, done=True)
        self.assertEqual(self.command("done", str(first["id"])), expected)
        self.assertEqual(self.command("done", str(first["id"])), expected)
        self.assertEqual(self.command("list"), [expected, second])

    def test_blank_title_preserves_rows_ac4(self):
        original = self.command("add", "Keep me")
        self.command("add", " \t ", status=2)
        self.assertEqual(self.command("list"), [original])

    def test_invalid_and_unknown_ids_preserve_rows_ac5(self):
        original = self.command("add", "Keep me")
        for value, status in [("999", 1), ("0", 2), ("-1", 2), ("abc", 2)]:
            with self.subTest(value=value):
                self.command("done", value, status=status)
                self.assertEqual(self.command("list"), [original])

    def test_missing_parent_reports_storage_error_ac6(self):
        missing = Path(self.temp.name) / "absent" / "tasks.sqlite3"
        self.command("list", db=missing, status=1)
        self.assertFalse(missing.parent.exists())

    def test_corrupt_database_preserved_ac6(self):
        damaged = b"this is not a SQLite database\n"
        self.db.write_bytes(damaged)
        self.command("list", status=1)
        self.assertEqual(self.db.read_bytes(), damaged)

    def test_stopped_database_backup_restore_ac7(self):
        first = self.command("add", "Before backup")
        backup = Path(self.temp.name) / "backup.sqlite3"
        shutil.copyfile(self.db, backup)
        self.command("add", "After backup")
        self.assertEqual(len(self.command("list")), 2)
        shutil.copyfile(backup, self.db)
        self.assertEqual(self.command("list"), [first])


if __name__ == "__main__":
    unittest.main()
