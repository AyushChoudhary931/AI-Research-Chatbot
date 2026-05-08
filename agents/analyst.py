from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from graph.state import ResearchState
import os
from dotenv import load_dotenv


load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3
)


def analyst_node(state: ResearchState) -> dict:
    """
    Analyst Agent:
    Reads raw search results and extracts:
    - Key facts
    - Themes
    - Conflicting viewpoints
    - Knowledge gaps
    """

    print("[Analyst] Analyzing search results...")

    sources = "\n\n".join(
        f"Source: {r['title']}\n{r['content']}"
        for r in state["search_results"]
    )

    # Prompt Template
    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert research analyst.

        Given the following web sources about "{topic}", extract and organize:

        1. Key facts and statistics
        2. Main themes or arguments
        3. Conflicting viewpoints (if any)
        4. Knowledge gaps

        Web Sources:
        {sources}

        Provide a well-structured analysis.
        """
    )

    # Create chain
    chain = prompt | llm

    # Invoke chain
    response = chain.invoke({
        "topic": state["topic"],
        "sources": sources
    })

    analysis = response.content

    print("[Analyst] Analysis complete.")

    return {
        "analysis": analysis
    }