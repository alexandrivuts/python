def process_input(data):
    if isinstance(data, dict):
        # Если передан словарь, найдем три ключа с самыми маленькими значениями
        sorted_items = sorted(data.items(), key=lambda x: x[1])
        smallest_keys = dict(sorted_items[:3])
        return smallest_keys
    elif isinstance(data, list):
        # Если передан список, удалите все нулевые элементы и найдите произведение первого и второго положительных элементов
        data = [x for x in data if x != 0]
        if len(data) >= 2:
            product = data[0] * data[1]
            return product
        else:
            return "Недостаточно положительных элементов в списке"
    elif isinstance(data, int):
        # Если передано число, определите количество разрядов
        num_digits = len(str(abs(data)))
        return num_digits
    elif isinstance(data, str):
        # Если передана строка, определите, сколько раз каждый символ встречается в строке
        char_count = {}
        for char in data:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
    else:
        return "Неподдерживаемый тип данных"

# Примеры использования функции:
input_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1, 'g':0}
input_list = [0, 3, 7, 0, 2, 5]
input_int = 12345
input_str = "hello, world!"

result_dict = process_input(input_dict)
result_list = process_input(input_list)
result_int = process_input(input_int)
result_str = process_input(input_str)

print("Результат для словаря:", result_dict)
print("Результат для списка:", result_list)
print("Результат для числа:", result_int)
print("Результат для строки:", result_str)
