import random
import string


class DataHelper:
    @staticmethod
    def generate_name() -> str:
        # Генерирует Имя пользователя (простую комбинацию символов)
        name_length = random.randint(3, 6)
        name = ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(name_length)
        )

        return name

    @staticmethod
    def generate_login() -> str:
        # Генерирует Email(логин) пользователя
        login_length = random.randint(3, 10)
        login = ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(login_length)
        )

        domains = ["ya.ru", "gmail.com", "mail.ru"]
        domain = random.choice(domains)

        return f"{login}@{domain}".lower()

    @staticmethod
    def generate_password(min_length=6, max_length=12) -> str:
        # Генерирует пароль пользователя
        length = random.randint(min_length, max_length)
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))

        return password