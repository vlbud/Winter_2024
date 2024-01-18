
"""
Задание 2-2
"""

lst = [1, 2, 3, 4, 5, 66, 7, 8, 9, 0]
a = lst[0]
for i in lst:
    if a > i:
        a = i
print(a)


lst = [1, 3, 4, 5, 6, 7, 8, 0]
print(min(lst))
