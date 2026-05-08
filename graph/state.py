from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class ResearchState(TypedDict):
    """Shared state passed between all agents in the pipeline."""
    topic: str                              
    search_results: list[dict]              
    analysis: str                           
    critique: str                           
    final_report: str                       
    messages: Annotated[list, add_messages] 
