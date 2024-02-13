def func():
    n = 1
    while True:
        if n % 2 == 0:
            yield - n
            n += 1
        else:
            yield n
            n += 1


gf = func()
for i in range(10):
    print(next(gf), end=' ')

print()
