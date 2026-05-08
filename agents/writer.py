from langchain_openai import ChatOpenAI
from config.settings import MODEL_NAME
from graph.state import ResearchState
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.3
)


def writer_node(state: ResearchState) -> dict:
    """
    Writer Agent: Synthesizes all prior work into a clear,
    well-structured research report for the end user.
    """
    print("[Writer] Writing final report...")

    prompt = f"""
    You are a professional research writer. Using the analysis and critique below,
    write a comprehensive, well-structured report on: "{state['topic']}"

    ## Analysis
    {state['analysis']}

    ## Critic's Feedback
    {state['critique']}

    Write a final report with:
    - Executive Summary (2-3 sentences)
    - Background & Context
    - Key Findings
    - Different Perspectives
    - Conclusion

    Use clear headings and be thorough but concise.
    """

    response = model.invoke(prompt)

    report = response.content

    print("[Writer] Report complete.")

    return {"final_report": report}