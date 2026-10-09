import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layput import style_background_dashboard, style_base_layout
from src.components.footer import footer_dashboard
def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    
    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()

def teacher_screen_login():
    col1, col2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with col1:
        header_dashboard()
    with col2:
        if st.button("Go back to Home", type="secondary", key="loginbackbutton", shortcut="control + backspace"):
            st.session_state["login_type"] = None
            st.rerun()
        
    st.header("Login using password",text_alignment="center")
    st.space()
    st.space()
    teacher_username = st.text_input("Enter username", placeholder="Kshitiz nagar")
    teacher_password = st.text_input("Enter password", type="password", placeholder="Enter your password")
    
    st.divider()
    btn1, btn2 = st.columns(2, vertical_alignment="center")
    with btn1:
        st.button("Login", icon=":material/passkey:", shortcut="command + enter", width="stretch")
    with btn2:
        if st.button("Register Instead", icon=":material/passkey:", type="primary", width="stretch"):
            st.session_state.teacher_login_type = "register"
            st.rerun()
    footer_dashboard()
    
    
    
    
def teacher_screen_register():
    col1, col2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with col1:
        header_dashboard()
    with col2:
        if st.button("Go back to Home", type="secondary", key="loginbackbutton", shortcut="control + backspace"):
            st.session_state["login_type"] = None
            st.rerun()
    st.header("Register your teacher profile",text_alignment="center")
    st.space()
    st.space()
    teacher_username = st.text_input("Enter username", placeholder="Kshitiz@123")
    teacher_name = st.text_input("Enter your full-name", placeholder="Kshitiz nagar")
    teacher_password = st.text_input("Enter password", type="password", placeholder="Enter your password")
    teacher_password_confirm = st.text_input("Confirm password", type="password", placeholder="Enter your password")
        
    st.divider()
    btn1, btn2 = st.columns(2, vertical_alignment="center")
    with btn1:
        st.button("Register now", icon=":material/passkey:", shortcut="command + enter", width="stretch", type="primary")
    with btn2:
        if st.button("Login Instead", icon=":material/passkey:", width="stretch"):
            st.session_state.teacher_login_type = "login"
            st.rerun()
    footer_dashboard()