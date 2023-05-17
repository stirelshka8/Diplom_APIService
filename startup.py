import os
from sys import platform


def exists_file(command: str):
    if os.path.exists(".env"):
        os.system(command)
    else:
        print("Отсутствует файл <.env>")


def startup():
    if platform == "linux" or platform == "linux2":
        exists_file("python3 manage.py runserver")
    elif platform == "darwin":
        exists_file("python3 manage.py runserver")
    elif platform == "win32":
        exists_file("python manage.py runserver")


if __name__ == '__main__':
    startup()
