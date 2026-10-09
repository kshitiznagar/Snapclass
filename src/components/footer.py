import streamlit as st

def footer_home():
    st.markdown(
            f"""
            <div style = "display: flex; flex-direction: column; align-item: center; justify-content:center; margin-bottom:30px; margin-top:20px; color:black">
                <p style = 'text-align:center; color:E0E3FF'>Made with❤️ by Kshitiz Nagar</p>
            </div>
            """,unsafe_allow_html=True,anchors=False)