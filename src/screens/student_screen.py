import streamlit as st

def student_screen():
    st.header("student screen")
    if st.button("Back"):
        st.session_state['login_type'] = None