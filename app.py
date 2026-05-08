import streamlit as st

from memory.database import init_db
from ui.styles import load_css
from ui.sidebar import render_sidebar
from ui.home import render_home
from ui.session_view import render_session
from ui.footer import render_footer


# PAGE CONFIG
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔍",
    layout="wide"
)

# INIT DATABASE
init_db()

# LOAD GLOBAL CSS
load_css()

# SESSION STATE
if "active_thread" not in st.session_state:
    st.session_state.active_thread = None


# SIDEBAR
render_sidebar()


# MAIN AREA
active_id = st.session_state.active_thread

if active_id:
    render_session(active_id)
else:
    render_home()


# FOOTER
render_footer()