import streamlit as st


def render_footer():

    st.divider()

    st.markdown("""
    <div class="footer">

    Built by 
    Ayush Choudhary

    <br><br>

    <a
        href="https://github.com/AyushChoudhary931">
        GitHub Profile
    </a>

    </div>
    """, unsafe_allow_html=True)