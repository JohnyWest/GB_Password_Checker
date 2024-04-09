import hashlib
def check_password(password):
    if len(password) <8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def main():
    password = input("Введите пароль: ")
    if check_password(password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print("Пароль прошел проверку на сложность и его хэш-значение: ", hashed_password)
    else:
        print("Пароль не удовлетворяет условиям сложности")

if __name__ == "__main__":
    main() 