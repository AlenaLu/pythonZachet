n = int(input("Колчество км спортсмен пробежал в 1й день: "))

y = int(input("Процент нормы дня: "))
x = int(input("Количество дней для бега: "))

for total_km in range(x):
    total_km += (n * y) / 10

print("Всего за", x, "дней спортстмен пробежит", total_km, "км")


