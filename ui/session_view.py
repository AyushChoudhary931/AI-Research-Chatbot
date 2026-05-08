import streamlit as st

from memory.database import (
    get_session,
    update_session
)

from graph.pipeline import run_research


def render_session(active_id):

    session = get_session(active_id)

    if session is None:

        st.error("Session not found.")

        return

    st.title(f"{session['topic']}")

    st.caption(
        f"Thread ID: `{session['thread_id']}`"
        f" • {session['created_at']}"
    )

    # DONE
    if (
        session["status"] == "done"
        and session["report"]
    ):

        st.success("Research complete!")

        st.markdown(
            f"""
            <div class="report-box">
            {session["report"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.download_button(
            "⬇ Download Report",
            data=session["report"],
            file_name=(
                f"{session['topic'][:40]}"
                f".md"
            ),
            mime="text/markdown"
        )

    # RUNNING
    elif session["status"] == "running":

        st.info(
            "This session is still running "
            "(or was interrupted)."
        )

        if st.button("Re-Run"):

            with st.spinner("Agents working…"):

                try:

                    report = run_research(
                        session["topic"],
                        active_id
                    )

                    update_session(
                        active_id,
                        "done",
                        report
                    )

                    st.rerun()

                except Exception as e:

                    update_session(
                        active_id,
                        "error"
                    )

                    st.error(f"Error: {e}")

    # ERROR
    elif session["status"] == "error":

        st.error(
            "This session encountered an error."
        )

        if st.button("Retry"):

            update_session(
                active_id,
                "running"
            )

            st.rerun()