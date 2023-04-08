import os
from flask import g

class AuthService():

    @classmethod
    def validate_unique_username(cls, username):
        """
        :param username: str
        :return: bool
        """
        for user in g.mydb["users"]:
            if user.get("username") == username:
                return False
        return True
    

    @classmethod
    def validate_password(cls, password):
        """
        :param password: str
        :return: bool
        """
        if len(password) < 4:
            return False
        return True
    

    @classmethod
    def register_user(cls, username, password):
        """
        :param username: str
        :param password: str
        :return: bool
        """
        user = {
            "username": username,
            "password": password
        }
        g.mydb["users"].append(user)
        return True
    

    @classmethod
    def login_user(cls, username, password):
        """
        :param username: str
        :param password: str
        :return: bool
        """
        for user in g.mydb["users"]:
            if user.get("username") == username:
                if user.get("password") == password:
                    return True
        return False

