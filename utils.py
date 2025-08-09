import streamlit as st

def load_css():
    """Load CSS from style.css into Streamlit."""
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
