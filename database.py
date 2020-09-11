from pymongo import MongoClient
from hashlib import sha256


class Database:
    def __init__(self, location="localhost", port=27017):
        self.location = location
        self.port = port
        self.client = MongoClient()

        self.db = self.client.web_app_database
        self.files = self.db.files
        self.users = self.db.users

    def not_empty_login(self, username: str, password: str):
        """Check if user inputs are empty"""
        if username == "" or password == "":
            return False
        else:
            return True

    def validate_username(self, username: str):
        if len(username) >= 4:
            return True
        return False

    def validate_password(self, password: str):
        if len(password) >= 12:
            return True
        return False

    def hash_password(self, password: str) -> str:
        return sha256(password.encode()).hexdigest()

    def check_user(self, username: str):
        if self.users.find_one({"username": username}):
            return True
        return False

    def create_user(self, username: str, password: str):
        if not self.check_user(username):
            password = self.hash_password(password)
            entry = {"username": username, "password": password, "files": []}
            self.users.insert_one(entry)
            return True
        return False

    def check_password(self, username: str, password: str):
        user = self.users.find_one({"username": username})
        if user is not None:
            if user['password'] == self.hash_password(password):
                return True
        return False

    def get_files(self, username: str):
        files = self.users.find_one({"username": username})
        return files
