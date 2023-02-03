class User:
    def __init__(self, email:str, password : str):
        self.__email = email
        self.__password = password
        self.__id = id(self)

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def id(self):
        return self.__id
