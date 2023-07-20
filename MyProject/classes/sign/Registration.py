class Registration():
    def create_user(self,users_list):
        users_list.append({
            "first_name" : input("Введите имя: "),
            "last_name" : input("Введите фамилию: "),
            "birthday" : input("Введите дату рождения: "),
            "gender" : input("Введите пол: "),
            "login" : input("Введите логин: "),
            "password" : input("Введите пароль: ")
            },)
        return users_list
