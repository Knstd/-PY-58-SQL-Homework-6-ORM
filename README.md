# -PY-58-SQL-Homework-6-ORM
Домашнее задание к лекции «Python и БД. ORM»


Задание 1

Составить модели классов SQLAlchemy по схеме:

Интуитивно необходимо выбрать подходящие типы и связи полей.


Задание 2

Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python скрипт, который:

    Подключается к БД любого типа на ваш выбор (например, к PostgreSQL).
    Импортирует необходимые модели данных.
    Выводит издателя (publisher), имя или идентификатор которого принимается через input().


Задание 3 (необязательное)

Заполните БД тестовыми данными.

Тестовые данные берутся из папки fixtures. Пример содержания в JSON файле.

Возможная реализация: прочитать json-файл, создать соотведствующие экземляры моделей и сохранить в БД.
Пример реализации, но сначала попытайтесь самостоятельно ;)
Общие советы:

    Параметры подключения к БД следует выносить в отдельные переменные (логин, пароль, название БД и пр.)
    Загружать значения лучше из окружения ОС, например через os.getenv()
    Заполнять данными можно вручную или выполнить необязательное задание 3
