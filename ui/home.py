import streamlit as st

from memory.database import (
    create_session,
    update_session
)

from graph.pipeline import run_research


def render_home():

    st.title("🔍 AI Research Agent")

    # st.markdown("""
    # <div class="report-box">

    # <h3>AI-Powered Multi-Agent Research System</h3>

    # <p>
    # Perform deep research using autonomous AI agents powered by
    # LangGraph, OpenAI, Tavily Search, SQLite memory,
    # and LangSmith observability.
    # </p>

    # </div>
    # """, unsafe_allow_html=True)

    # EXPLAINER
    with st.expander("⚙ How it works"):

        st.markdown("""

| Step | Agent | What it does |
|------|-------|-------------|
| 1 | **Researcher** | Live web search via Tavily |
| 2 | **Analyst** | Extracts key facts & themes |
| 3 | **Critic** | Reviews for bias & gaps |
| 4 | **Writer** | Writes the final report |

State is passed between agents via a LangGraph state graph.

Every session is saved to SQLite.

All runs are traced in LangSmith.

        """)

    st.divider()

    topic = st.text_input(
        "What do you want to research?",
        placeholder=(
            "e.g. The impact of AI on "
            "software engineering jobs"
        )
    )

    if st.button(
        "Start Research",
        disabled=not topic,
        type="primary"
    ):

        thread_id = create_session(topic)

        st.session_state.active_thread = thread_id

        with st.spinner(
            "Agents working… this takes ~30–60 seconds."
        ):

            try:

                report = run_research(
                    topic,
                    thread_id
                )

                update_session(
                    thread_id,
                    "done",
                    report
                )

            except Exception as e:

                update_session(
                    thread_id,
                    "error"
                )

                st.error(
                    f"Pipeline error: {e}"
                )

        st.rerun()