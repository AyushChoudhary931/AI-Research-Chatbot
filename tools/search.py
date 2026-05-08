from tavily import TavilyClient
from config.settings import TAVILY_API_KEY, MAX_SEARCH_RESULTS


def web_search(query: str) -> list[dict]:
    """Search the web and return top results."""
    client = TavilyClient(api_key=TAVILY_API_KEY)
    response = client.search(query=query, max_results=MAX_SEARCH_RESULTS)
    return [
        {"title": r["title"], "url": r["url"], "content": r["content"]}
        for r in response.get("results", [])
    ]
