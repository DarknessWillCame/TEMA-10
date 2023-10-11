class NameLengthError(Exception):
    def __init__(self, message):
        self.message = message

def lower_case_username(value):
    if len(value) < 3:
        raise NameLengthError('Длина имени должна быть больше 2-ух символов')

class Student:
    def __init__(self, name, age):
        self.name = lower_case_username(name)
        self.age = age

try:
    lower_case_username('Ли')
except NameLengthError as err:
    print('Ошибка:', err)

try:
    Student('Ли', 25)
except NameLengthError as err:
    print('Ошибка:', err)

try:
    Student('Лии', 25)
except NameLengthError as err:
    print('Ошибка:', err)
finally:
    print('Учётная запись студента создана успешно')
