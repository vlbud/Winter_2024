"""
Задача 1-2
"""
x = int(input())
y = int(input())

a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
if a > b and a > c and a > d and a > e:
    print("Наибольшее число", a)

if b > a and b > c and d > e:
    print("Наибольшее число", b)

if c > a and c > b and c > d and c > e:
    print("Наибольшее число", c)

if d > a and d > b and d > c and d > e:
    print("Наибольшее число", d)

if e > a and e > b and e > c and e > d:
    print("Наибольшее число", e)
