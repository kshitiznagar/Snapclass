import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layput import style_background_dashboard, style_base_layout
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login


def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"""Welcome, {teacher_data["name"]}""")

def login_teacher(username, password):
    if not username or not password:
        return False
    teacher = teacher_login(username, password)
    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    
    return False


def register_teacher(teacher_username, teacher_name, teacher_password, teacher_password_confirm):
    if not teacher_username or not teacher_name or not teacher_password:
        return False, "All fields are required!"
    if check_teacher_exists(teacher_username):
        return False, "username is already taken"
    if teacher_password != teacher_password_confirm:
        return False, "password doesn't match"
    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Successfully created! Login now"
    except Exception as e:
        return False, "Unexpected error"
    
    
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
        if st.button("Login", icon=":material/passkey:", shortcut="command + enter", width="stretch"):
            if login_teacher(teacher_username, teacher_password):
                st.toast(f"Welcome back!", icon="👋🏻")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Username and password combo")
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
        if st.button("Register now", icon=":material/passkey:", shortcut="command + enter", width="stretch", type="primary"):
            success, message = register_teacher(teacher_username, teacher_name, teacher_password, teacher_password_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                error_slot = st.container(height=56, border=False)
                with error_slot:
                    if not success:
                        st.error(message)
    with btn2:
        if st.button("Login Instead", icon=":material/passkey:", width="stretch"):
            st.session_state.teacher_login_type = "login"
            st.rerun()
    footer_dashboard()