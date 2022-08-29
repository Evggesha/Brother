year_of_birth = int(input("Введите год своего рождения: "))
year_of_today = int(input("Введите год рождения своего брата: "))
if year_of_today>year_of_birth:
    print("Вы старше своего брата на" , year_of_today-year_of_birth , "лет")
elif year_of_today<year_of_birth:
    print("Ваш брат старше Вас на" , year_of_birth-year_of_today , "лет")
else:
    print("Вы одногодки")

