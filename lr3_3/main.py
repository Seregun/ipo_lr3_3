day = int(input("Введите день: ")) # Ввод дня
month = int(input("Введите месяц: ")) # Ввод месяца
if (month == 3 and day >= 1) or (month == 4) or (month == 5) or (month == 6 and day <= 31): # Проверка на время года "Весна"
    season = "Весна" # Время года "Весна"
elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 9 and day <= 31): # Проверка на время года "Лето"
    season = "Лето" # Время года "Лето"
elif (month == 9 and day >= 1) or (month == 10) or (month == 11) or (month == 12 and day <= 30): # Проверка на время года "Осень"
    season = "Осень" # Время года "Осень"
else: # Если не "Весна", "Лето" или "Осень"
    season = "Зима" # Время года "Зима"
print(f"Эта дата относится к времени года: {season}") # Вывод времени года