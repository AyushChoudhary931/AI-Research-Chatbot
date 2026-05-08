"""
LangGraph pipeline with:
  • SqliteSaver  — persists every agent's state to SQLite after each step
  • thread_id    — isolates state per research session (multiple chats)
  • LangSmith    — auto-traces every invocation via env vars
"""
import sqlite3
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver

from graph.state import ResearchState
from agents.researcher import researcher_node
from agents.analyst   import analyst_node
from agents.critic    import critic_node
from agents.writer    import writer_node
from config.settings  import DB_PATH


def _build_graph() -> StateGraph:
    graph = StateGraph(ResearchState)

    graph.add_node("researcher", researcher_node)
    graph.add_node("analyst",    analyst_node)
    graph.add_node("critic",     critic_node)
    graph.add_node("writer",     writer_node)

    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "analyst")
    graph.add_edge("analyst",    "critic")
    graph.add_edge("critic",     "writer")
    graph.add_edge("writer",     END)

    return graph


def get_pipeline():
    """
    Compile the graph with a SqliteSaver checkpointer.
    The same DB file is shared with the sessions table in memory/database.py.
    check_same_thread=False is required for Streamlit's multi-thread model.
    """
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    checkpointer = SqliteSaver(conn=conn)
    return _build_graph().compile(checkpointer=checkpointer)


# Single compiled instance reused across the app session
_pipeline = None

def _get_pipeline_singleton():
    global _pipeline
    if _pipeline is None:
        _pipeline = get_pipeline()
    return _pipeline


def run_research(topic: str, thread_id: str) -> str:
    """
    Run (or resume) the research pipeline for a given thread.
    Passing the same thread_id a second time resumes from the last checkpoint.
    """
    pipeline = _get_pipeline_singleton()
    config   = {"configurable": {"thread_id": thread_id}}

    result = pipeline.invoke(
        {"topic": topic, "messages": []},
        config=config
    )
    return result["final_report"]


def get_thread_state(thread_id: str) -> dict | None:
    """
    Retrieve the last saved checkpoint state for a thread.
    Returns None if the thread has never been run.
    """
    pipeline = _get_pipeline_singleton()
    config   = {"configurable": {"thread_id": thread_id}}
    state    = pipeline.get_state(config)
    return state.values if state else None