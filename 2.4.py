try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = a / b

except ZeroDivisionError:
    print("Ошибка: Деление на ноль")

except ValueError:
    print("Ошибка: Введите корректное число")

else:
    print(f"Результат деления: {c}")

finally:
    print("Программа завершена")

print("Программа закончила выполнение")
