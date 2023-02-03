import json
from  app.model.User import User
def check_existence(email : str) -> bool:
    try:
        with open("app/db/users.json", "r") as f:
            file = json.loads(f.read())
            f.close()

        for element in file:
            if element["email"]  == email:
                return True

        return False

    except FileNotFoundError :
        print("Error comprobando existencia de usuario")

def get_users(email = ""):
    try:
        with open("app/db/users.json", "r") as f:
            file = json.loads(f.read())
            f.close()

        if email:
            for i, element in enumerate(file):
                if element["email"] == email:
                    return file[i]

        else:
            elements = [element for element in file]
            return elements

    except FileNotFoundError :
        print("Error obteniendo todos los usuarios")


def register_user(email: str, password : str):
    try:
        other_user = User(email, password)
        users = get_users()
        users.append({
            "id" : other_user.id,
            "email": other_user.email,
            "password" : other_user.password
        })
        with open("app/db/users.json", "w") as f:
            f.write(json.dumps(users))
        return True

    except Exception:
        print("Error guardando un nuevo usuario")