import os
from sys import platform


def exists_file(command: str):
    if os.path.exists(".env"):
        try:
            os.system(command)
        except KeyboardInterrupt:
            print("Выполнение завершено!")
    else:
        print("Отсутствует файл <.env>\n\n")
        print("Введите YES для создания файла и установки зависимостей")
        anserw_env = input('-->')

        if anserw_env.upper() == 'YES':
            secret = input('Введите секретный ключ -->')
            debug = input('Укажите True для включения дебаг режима, False для его оключения -->')
            db_name = input('Имя базы данных -->')
            db_user = input('Пользователь базы данных -->')
            db_pass = input('Пароль базы данных -->')
            db_host = input('Хост базы данных -->')
            db_port = input('Порт базы данных -->')

            env_write = (f'SECRET_KEY={secret}\n'
                         f'DEBUG={debug}\n'
                         f'DB_ENGINE=django.db.backends.postgresql\n'
                         f'DB_NAME={db_name}\n'
                         f'DB_USER={db_user}\n'
                         f'DB_PASSWORD={db_pass}\n'
                         f'DB_HOST={db_host}\n'
                         f'DB_PORT={db_port}')

            with open('.env', 'w') as files_env:
                files_env.write(env_write)

            if platform == "linux" or platform == "linux2":
                os.system("python3 -m venv venv")
                os.system("source venv/bin/activate")
                os.system("pip install -r req.txt")
                os.system("python manage.py makemigrations backendAPI")
                os.system("python manage.py migrate backendAPI")
                os.system("python manage.py migrate")
                print("\n\n -------------ЗАВЕРШЕНО!------------- \n\n")
            elif platform == "darwin":
                os.system("python3 -m venv venv")
                os.system("source venv/bin/activate")
                os.system("pip install -r req.txt")
                os.system("python manage.py makemigrations backendAPI")
                os.system("python manage.py migrate backendAPI")
                os.system("python manage.py migrate")
                print("\n\n -------------ЗАВЕРШЕНО!------------- \n\n")
            elif platform == "win32":
                os.system("python -m venv venv")
                os.system("venv/bin/activate")
                os.system("pip install -r req.txt")
                os.system("python manage.py makemigrations backendAPI")
                os.system("python manage.py migrate backendAPI")
                os.system("python manage.py migrate")
                print("\n\n -------------ЗАВЕРШЕНО!------------- \n\n")


def startup():
    if platform == "linux" or platform == "linux2":
        exists_file("python3 manage.py runserver")
    elif platform == "darwin":
        exists_file("python3 manage.py runserver")
    elif platform == "win32":
        exists_file("python manage.py runserver")


if __name__ == '__main__':
    startup()
