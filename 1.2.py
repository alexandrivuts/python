str1 = input("Введите строку: ")

words = str1.split()

words1 = 0
words2 = 0

for word in words:
    strlen = len(word)
    if strlen % 2 == 0:
        words1 += 1
    else:
        words2 += 1

print(f"Количество слов четной длины: {words1}")
print(f"Количество слов нечетной длины: {words2}")
