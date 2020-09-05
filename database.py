from pymongo import MongoClient
from hashlib import sha256


client = MongoClient("localhost", 27017)
db = client.web_app_database

files = db.files
users = db.users


def not_empty_login(username: str, password: str):
    """Check if user inputs are empty"""
    if username == "" or password == "":
        return False
    else:
        return True


def validate_username(username: str):
    if len(username) >= 4:
        return True
    return False


def validate_password(password: str):
    if len(password) >= 12:
        return True
    return False


def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()


def check_user(username: str):
    if users.find_one({"username": username}):
        return True
    return False


def create_user(username: str, password: str):
    if not check_user(username):
        password = hash_password(password)
        entry = {"username": username, "password": password, "files": []}
        users.insert_one(entry)
        return True
    return False


def check_password(username: str, password: str):
    user = users.find_one({"username": username})
    if user is not None:
        if user['password'] == hash_password(password):
            return True
    return False


def get_files(username: str):
    files = users.find_one({"username": username})
    return files
