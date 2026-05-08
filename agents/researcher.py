from tools.search import web_search
from graph.state import ResearchState


def researcher_node(state: ResearchState) -> dict:
    """
    Researcher Agent: Gathers raw information from the web
    about the given topic.
    """
    print(f"[Researcher] Searching for: {state['topic']}")
    results = web_search(state["topic"])
    print(f"[Researcher] Found {len(results)} sources.")
    return {"search_results": results}
