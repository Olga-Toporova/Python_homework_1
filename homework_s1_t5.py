'''
5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
ними в 2D пространстве. 

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''

x1 = int(input("Введите координату A(x): "))
y1 = int(input("Введите координату A(y): "))
x2 = int(input("Введите координату B(x): "))
y2 = int(input("Введите координату B(y): "))
print(round(((x2 - x1)**2 + (y2-y1)**2)**0.5, 3))
