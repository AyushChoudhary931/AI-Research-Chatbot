"""
LangSmith observability.
Importing this module is enough — the env vars set in settings.py
make LangChain/LangGraph auto-trace every invocation.
Call `trace_run()` to attach extra metadata (topic, thread_id) to a run.
"""
from langsmith import Client
from config.settings import DB_PATH   # noqa: F401 — ensures settings are loaded first
import os


def get_client() -> Client | None:
    """Return a LangSmith client, or None if no API key is configured."""
    key = os.getenv("LANGSMITH_API_KEY", "")
    if not key:
        return None
    return Client()


def trace_run(thread_id: str, topic: str, run_id: str = None) -> None:
    """
    Attach searchable metadata to a LangSmith trace.
    Useful for filtering runs by topic or session in the LangSmith UI.
    """
    client = get_client()
    if client is None or run_id is None:
        return
    try:
        client.update_run(
            run_id,
            extra={"metadata": {"thread_id": thread_id, "topic": topic}}
        )
    except Exception:
        pass 


def langsmith_url() -> str | None:
    """Return the LangSmith project URL for display in the UI."""
    project = os.getenv("LANGSMITH_PROJECT", "research-agent")
    key     = os.getenv("LANGSMITH_API_KEY", "")
    if not key:
        return None
    return f"https://smith.langchain.com/projects/{project}"