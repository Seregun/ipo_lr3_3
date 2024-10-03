day = int(input("Введите день: ")) # Ввод дня
month = int(input("Введите месяц: ")) # Ввод месяца
if (day < 1 or month < 1): # Проверка на существование даты
    print("Невеная дата!") # Такой даты нету
else: # Если дата существует
    if (month == 3 and day >= 1 and day <= 31) or (month == 4 and day <= 30) or (month == 5 and day <= 31): # Проверка на время года "Весна"
       season = "Весна" # Время года "Весна"
    elif (month == 6 and day >= 1 and day <= 30) or (month == 7 and day <= 31) or (month == 8 and day <= 31): # Проверка на время года "Лето"
        season = "Лето" # Время года "Лето"
    elif (month == 9 and day >= 1 and day <= 30) or (month == 10 and day <= 31) or (month == 11 and day <= 30): # Проверка на время года "Осень"
       season = "Осень" # Время года "Осень"
    elif (month == 12 and day >= 1 and day <= 31) or (month == 1 and day <= 31) or (month == 2 and day <= 28): # Если не "Весна", "Лето" или "Осень"
        season = "Зима" # Время года "Зима"
    else: # Если не подходит ни к чему
        season = "Ошибка!" # Неверная дата
        print("Неверная дата!") # Неверно заданная дата
print(f"Эта дата относится к времени года: {season}") # Вывод времени года
