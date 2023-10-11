class EmptyFileError(Exception):
    def __init__(self, message):
        self.message = message

def open_file(path, mode):
    try:
        with open(path, mode) as file:
            content = file.read()
            if content == '':
                raise EmptyFileError('Файл пустой')
            else:
                print('Содержимое файла:', content)
    except EmptyFileError as err:
        print('Ошибка:', err)

open_file('./Tema10_2_empty_file.txt', 'r')
open_file('./Tema10_2_filled_file.txt', 'r')
