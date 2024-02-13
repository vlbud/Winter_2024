nums = list(map(int, input('Введите список целых чисел: ').split()))


def func1(nums):
    for i in nums:
        if i % 2 == 1:
            yield i


gf = func1(nums)
for s in gf:
    print(s, end= " ")
