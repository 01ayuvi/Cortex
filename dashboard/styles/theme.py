import streamlit as st


def apply_theme():
    st.markdown("""
    <style>

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
    }

    div[data-testid="metric-container"]{
        background:#1e1e1e;
        border:1px solid #333;
        padding:18px;
        border-radius:14px;
    }

    .stButton>button{
        width:100%;
        border-radius:10px;
        height:45px;
        font-weight:bold;
    }

    section[data-testid="stSidebar"]{
        border-right:1px solid #2c2c2c;
    }

    </style>
    """, unsafe_allow_html=True)