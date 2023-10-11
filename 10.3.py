def calc(value):
    try:
        converted_value = int(value)

        return 2 + converted_value;
    except ValueError as err:
        print('Неподходящий тип данных. Ожидалось число.')


print(calc(0))
print(calc(100))
print(calc('сто'))
