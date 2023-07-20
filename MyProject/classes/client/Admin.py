from .Moderator import *
class Admin(Moderator):
    def __init__(self, user_id, first_name, last_name, birthday, gender, login, password):
        super().__init__(user_id, first_name, last_name, birthday, gender, login, password)
        self.status = "admin"
    def delete_user_list(self, users_list):
        users_list.clear()
        print("База данных пуста")
                                # massiv - массиом данных
    def create_user_list(self, massiv, users_list):
        print(len(users_list))
        for i in range(len(users_list),len(massiv)):
            users_list.append()