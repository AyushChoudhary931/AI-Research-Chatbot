
import os
from dotenv import load_dotenv

load_dotenv()

# ── LLM & Search ──────────────────────────────────────────────
GOOGLE_API_KEY   = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY   = os.getenv("TAVILY_API_KEY")
MODEL_NAME       = "gemini-2.0-flash"
MAX_SEARCH_RESULTS = 5

# ── SQLite Database ───────────────────────────────────────────
DB_PATH = "research_agent.db"   

# ── LangSmith Observability ───────────────────────────────────
os.environ["LANGCHAIN_TRACING_V2"]  = "true"
os.environ["LANGCHAIN_PROJECT"]     = os.getenv("LANGSMITH_PROJECT", "research-agent")
os.environ["LANGCHAIN_API_KEY"]     = os.getenv("LANGSMITH_API_KEY", "")