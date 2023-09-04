import random

a = random.randint(1, 10)

k = 0

print("Давайте начнем игру! Угадайте число от 1 до 10.")

while True:
    b = input("Введите ваше число: ")
    k += 1

    try:
        b = int(b)
    except ValueError:
        print("Неверный ввод, повторите попытку.")
        continue

    if b < a:
        print("Ваше число меньше загаданного.")
    elif b > a:
        print("Ваше число больше загаданного.")
    else:
        print(f"Вы угадали с {k} попытки!")
        break
