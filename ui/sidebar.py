import streamlit as st

from memory.database import (
    list_sessions,
    delete_session
)


def render_sidebar():

    with st.sidebar:

        st.title("Research Agent")

        st.divider()

        if st.button(
            "New Research",
            use_container_width=True,
            type="primary"
        ):
            st.session_state.active_thread = None

        st.divider()

        st.subheader("Previous Sessions")

        sessions = list_sessions()

        if not sessions:
            st.caption(
                "No sessions yet. Start a new research above."
            )

        else:

            for s in sessions:

                col1, col2 = st.columns([5, 1])

                badge = {
                    "done": "✅",
                    "running": "⏳",
                    "error": "❌"
                }.get(s["status"], "❓")

                label = (
                    f"{badge} "
                    f"{s['topic'][:35]}"
                    f"{'…' if len(s['topic']) > 35 else ''}"
                )

                with col1:

                    if st.button(
                        label,
                        key=s["thread_id"],
                        use_container_width=True
                    ):
                        st.session_state.active_thread = s["thread_id"]

                with col2:

                    if st.button(
                        "🗑",
                        key=f"del_{s['thread_id']}"
                    ):

                        delete_session(s["thread_id"])

                        if (
                            st.session_state.active_thread
                            == s["thread_id"]
                        ):
                            st.session_state.active_thread = None

                        st.rerun()