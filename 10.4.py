# декоратор выводит тип значения,
# которое возвращено функцией
def print_type_function_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Тип результата:', type(result))
        return result
    return wrapper

@print_type_function_result
def add_numbers(a, b):
    return a + b

@print_type_function_result
def add_strings(a, b):
    return a + b

add_numbers(1, 2)
add_strings('100', '200')
