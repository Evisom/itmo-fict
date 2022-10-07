import math

sides = input("Введите 3 стороны треугольника (через пробел) \nЕсли треугольник односторонний введите одно число: ").split()
if len(sides) == 1:
    sides = sides*3
for i in range(0,len(sides)):
    sides[i] = int(sides[i])

if max(sides) < sum(sides)-max(sides):
    p = sum(sides)
    s = math.sqrt(p * (p-sides[0]) * (p - sides[1]) * (p - sides[2]) )
    print("Площадь треугольника:", s)
else:
    print("Треугольник не существует")

