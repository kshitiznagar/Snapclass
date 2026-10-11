from src.database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode("utf-8"), hashed.encode("utf-8"))

def check_teacher_exists(username):
    # checks unique username, returns false when username is already take
    response = supabase.table("teachers").select("user_name").eq("user_name", username).execute()
    return len(response.data) > 0


def create_teacher(username, password, name):
    data = {"user_name" : username, "password" : hash_pass(password), "name" : name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data


def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("user_name", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher["password"]):
            return teacher
        return None


def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data

def create_student(new_name, face_embedding = None, voice_embedding = None):
    data = {"name": new_name, "face_embedding": face_embedding, "voice_embedding": voice_embedding}
    response = supabase.table("students").insert(data).execute()
    return response.data
    