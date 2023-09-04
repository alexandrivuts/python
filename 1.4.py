random_sequence = "3125987490234567890"

number_counts = {}

for char in random_sequence:
    if char.isdigit():
        number = int(char)
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

print("Количество цифр в случайной последовательности:")
print(number_counts)
