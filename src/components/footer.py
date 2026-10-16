import streamlit as st


def footer_home():
    logo_url = "https://i.pinimg.com/1200x/31/c6/8b/31c68b4ceb0b1229ab6886b68de7011b.jpg"

    st.markdown(f"""
        <div style="margin-top: 1rem;display: flex;gap: 6px;justify-content: center;align-items: center">
            <p>Created By Abhinav Singh</p>
            <img src="{logo_url}" style="max-height: 25px;" />
        </div>
        """,
        unsafe_allow_html=True
    )
def footer_dashboard():
    logo_url = "https://i.pinimg.com/1200x/31/c6/8b/31c68b4ceb0b1229ab6886b68de7011b.jpg"

    st.markdown(f"""
        <div style="margin-top: 1rem;display: flex;gap: 6px;justify-content: center;align-items: center">
            <p style="color: black;">Created By Abhinav Singh</p>
            <img src="{logo_url}" style="max-height: 25px;" />
        </div>
        """,
        unsafe_allow_html=True
    )