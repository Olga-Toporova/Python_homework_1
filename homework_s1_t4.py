'''
4. Напишите программу, которая по заданному номеру четверти, показывает диапазон
возможных координат точек в этой четверти (x и y).
*Пример:*
'''

q = int(input("Введите номер четверти: "))
if 0 < q <= 4:
    if q == 1:
        print("x > 0, y > 0")
    elif q== 2:
        print("x < 0, y > 0")
    elif q==3:
        print("x < 0,y < 0")
    else:
        print("x > 0,y < 0")
else:
    print("Введено некорректное значение.")
    