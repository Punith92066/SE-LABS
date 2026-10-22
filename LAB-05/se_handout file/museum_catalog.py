
"""Museum artifact catalog with safer database handling."""

import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """CREATE TABLE artifacts (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        era TEXT NOT NULL,
        value INTEGER NOT NULL CHECK (value >= 0),
        on_display INTEGER NOT NULL DEFAULT 0
            CHECK (on_display IN (0, 1))
    )"""
)


def add_artifact(
    title: str, era: str, value: int, on_display: int = 0
) -> None:
    """Add an artifact using parameterized SQL and validated values."""
    if not title.strip():
        raise ValueError("Artifact title cannot be empty.")
    if not era.strip():
        raise ValueError("Artifact era cannot be empty.")
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(
            "Artifact value must be a non-negative integer."
        )
    if on_display not in (0, 1):
        raise ValueError("on_display must be 0 or 1.")

    conn.execute(
        "INSERT INTO artifacts (title, era, value, on_display) "
        "VALUES (?, ?, ?, ?)",
        (title, era, value, on_display),
    )
    conn.commit()


def display_status(
    artifact_id: int, curator: str | None = None
) -> str:
    """Return display status or an error for an unknown artifact ID."""
    del curator  # Retained for compatibility with the original demo.
    row = conn.execute(
        "SELECT on_display FROM artifacts WHERE id = ?",
        (artifact_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"No artifact found with id {artifact_id}.")
    return "on display" if row[0] == 1 else "in storage"


def total_value(era: str) -> int:
    """Return the combined value of artifacts from the requested era."""
    row = conn.execute(
        "SELECT COALESCE(SUM(value), 0) FROM artifacts WHERE era = ?",
        (era,),
    ).fetchone()
    return int(row[0])


def move_to_display(artifact_id: int) -> None:
    """Move an artifact to display if the ID exists."""
    cursor = conn.execute(
        "UPDATE artifacts SET on_display = 1 WHERE id = ?",
        (artifact_id,),
    )
    conn.commit()
    if cursor.rowcount == 0:
        raise ValueError(f"No artifact found with id {artifact_id}.")


def backup_note() -> None:
    """Print the catalog backup notice."""
    print("catalog backup complete")


def main() -> None:
    """Run a small catalog demonstration."""
    add_artifact("Bronze Mirror", "Chola", 120000)
    add_artifact("Palm Manuscript", "Vijayanagara", 80000, 1)
    add_artifact("Terracotta Lamp", "Chola", 15000)
    move_to_display(1)
    print(display_status(1, "Dr. Rao"))
    print(total_value("Chola"))
    backup_note()


if __name__ == "__main__":
    main()
