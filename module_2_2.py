first = int(input("Введите первое число: "))
second  = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first == second == third :
    print(3)
    print("Введённые три числа равны")
elif (first == second != third or
      first == third != second or
      second == third != first):
    print(2)
    print("Два числа из 3-х равны")
else:
    print(0)
    print("Все введённые числа разные 'не равны'")
