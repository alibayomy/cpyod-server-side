from data.users import users

class Users:
    USERNAME = "username"
    PASSWORD = "password"

    def validate_user(self, username, password):
        for user in users:
            if user[self.USERNAME] == username and user[self.PASSWORD] == password:
                return user["role"]
        raise ModuleNotFoundError