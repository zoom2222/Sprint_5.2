from attr import dataclass


@dataclass
class UserData:
    name: str = "Олег"
    email: str = "oleg_shatohin_22_333@ya.ru"
    password: str = "olegoleg"