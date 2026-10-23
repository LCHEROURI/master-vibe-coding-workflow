"""A local, single-user task tracker using only the Python standard library."""

import argparse
from contextlib import closing
import json
import sqlite3
import sys


def title(value):
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("title must not be blank")
    return value


def task_id(value):
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("ID must be a positive integer") from None
    if not 1 <= number <= 2**63 - 1:
        raise argparse.ArgumentTypeError("ID must fit a positive SQLite integer")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default="tasks.sqlite3", help="SQLite file path")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("add", help="add a task").add_argument("title", type=title)
    commands.add_parser("list", help="list every task in ID order")
    commands.add_parser("done", help="complete a task").add_argument("id", type=task_id)
    args = parser.parse_args()

    try:
        with closing(sqlite3.connect(args.db)) as db, db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS tasks ("
                "id INTEGER PRIMARY KEY, title TEXT NOT NULL, "
                "done INTEGER NOT NULL DEFAULT 0)"
            )
            if args.command == "add":
                cursor = db.execute("INSERT INTO tasks (title) VALUES (?)", (args.title,))
                rows = [(cursor.lastrowid, args.title, 0)]
            elif args.command == "done":
                cursor = db.execute("UPDATE tasks SET done = 1 WHERE id = ?", (args.id,))
                if cursor.rowcount == 0:
                    print(f"error: task {args.id} does not exist", file=sys.stderr)
                    return 1
                rows = db.execute(
                    "SELECT id, title, done FROM tasks WHERE id = ?", (args.id,)
                ).fetchall()
            else:
                rows = db.execute("SELECT id, title, done FROM tasks ORDER BY id").fetchall()
        tasks = [dict(id=id_, title=text, done=bool(done)) for id_, text, done in rows]
        print(json.dumps(tasks if args.command == "list" else tasks[0], ensure_ascii=False))
        return 0
    except sqlite3.Error as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
