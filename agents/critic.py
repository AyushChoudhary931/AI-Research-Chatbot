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


def critic_node(state: ResearchState) -> dict:
    """
    Critic Agent: Reviews the analyst's output for accuracy,
    bias, and completeness before the final report is written.
    """
    print("[Critic] Reviewing analysis for quality...")

    prompt = f"""You are a critical reviewer. Evaluate this research analysis on "{state['topic']}":

{state['analysis']}

Identify:
- Any factual claims that need verification
- Potential biases or one-sided arguments
- Missing perspectives or important context
- Overall quality score (1-10) with reasoning

Be concise and constructive."""

    response = model.invoke(prompt)

    critique = response.content

    print("[Critic] Review complete.")

    return {"critique": critique}