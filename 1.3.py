list = [1, 2, 3, 2, 4, 5, 6, 7, 4, 8, 0, 9, 0, 10]

count = {}

unique_elements = []

for item in list:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

for item in list:
    if count[item] == 1:
        unique_elements.append(item)

print("Элементы которые встречаются один раз:")
print(unique_elements)

zero_indices = [i for i, item in enumerate(list) if item == 0]

if len(zero_indices) >= 2:
    first_zero = zero_indices[0]
    last_zero = zero_indices[-1]
    zero_sum = sum(list[first_zero:last_zero])
    print(f"Сумма между первым и последним нулем: {zero_sum}")
else:
    print("Не хватает нулей в ряду.")