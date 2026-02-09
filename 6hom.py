try:
    value = input("Введіть число: ")
    number = int(value)          # спроба конвертації в int
    print("Ви ввели число:", number)
except ValueError:
    print("Помилка: введені дані не є числом")
