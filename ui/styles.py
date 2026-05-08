import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* GLOBAL */
    html, body, [class*="css"] {
        font-family: 'Georgia', serif;
        background-color: #0f1117;
        color: #f5f5f5;
    }

    /* MAIN CONTAINER */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #0f172a 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* BUTTONS */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.08);
        background: #1e293b;
        color: white;
        transition: all 0.2s ease;
        font-weight: 500;
        padding: 0.6rem 1rem;
    }

    .stButton > button:hover {
        background: #334155;
        border-color: #64748b;
    }

    /* INPUT */
    .stTextInput input {
        background-color: #111827;
        color: white;
        border-radius: 10px;
        border: 1px solid #374151;
    }

    /* REPORT BOX */
    .report-box {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 1.5rem;
        margin-top: 1rem;
    }

    /* FOOTER */
    .footer {
        text-align:center;
        color:#94a3b8;
        padding-top:20px;
        padding-bottom:10px;
    }

    </style>
    """, unsafe_allow_html=True)