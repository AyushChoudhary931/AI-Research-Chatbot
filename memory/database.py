"""
SQLite session store.
Tracks every research session (thread_id, topic, status, report).
LangGraph's SqliteSaver uses the SAME db file for its own checkpoint tables —
so everything lives in one place: research_agent.db
"""
import sqlite3
import uuid
from datetime import datetime
from config.settings import DB_PATH


def get_conn() -> sqlite3.Connection:
    """Return a thread-safe connection (used by both app and SqliteSaver)."""
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def init_db() -> None:
    """Create the sessions table if it doesn't exist yet."""
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                thread_id  TEXT PRIMARY KEY,
                topic      TEXT NOT NULL,
                status     TEXT DEFAULT 'running',   -- running | done | error
                report     TEXT,
                created_at TEXT NOT NULL
            )
        """)
        conn.commit()


def create_session(topic: str) -> str:
    """Insert a new session row and return its thread_id."""
    thread_id = str(uuid.uuid4())
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO sessions (thread_id, topic, created_at) VALUES (?, ?, ?)",
            (thread_id, topic, datetime.now().isoformat(timespec="seconds"))
        )
        conn.commit()
    return thread_id


def update_session(thread_id: str, status: str, report: str = None) -> None:
    """Mark a session as done/error and optionally save the report."""
    with get_conn() as conn:
        conn.execute(
            "UPDATE sessions SET status = ?, report = ? WHERE thread_id = ?",
            (status, report, thread_id)
        )
        conn.commit()


def list_sessions() -> list[dict]:
    """Return all sessions ordered newest-first."""
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT thread_id, topic, status, report, created_at "
            "FROM sessions ORDER BY created_at DESC"
        ).fetchall()
    return [
        {"thread_id": r[0], "topic": r[1],
         "status": r[2], "report": r[3], "created_at": r[4]}
        for r in rows
    ]


def get_session(thread_id: str) -> dict | None:
    """Fetch a single session by thread_id."""
    with get_conn() as conn:
        row = conn.execute(
            "SELECT thread_id, topic, status, report, created_at "
            "FROM sessions WHERE thread_id = ?", (thread_id,)
        ).fetchone()
    if not row:
        return None
    return {"thread_id": row[0], "topic": row[1],
            "status": row[2], "report": row[3], "created_at": row[4]}


def delete_session(thread_id: str) -> None:
    """Delete a session row (checkpoints remain in langgraph tables)."""
    with get_conn() as conn:
        conn.execute("DELETE FROM sessions WHERE thread_id = ?", (thread_id,))
        conn.commit()