a = [1, 2, 3, 4]
# f(1), f(2), f(3), f(4)
# lambda x: x**2
# ==
# def f(x):
#    return x**2

# map은 iterator라는 객체 , list로 casting 해주면 알아서 list가 next()해서 list에 담는다.
# it = list(map(lambda x: x**2, [1, 2, 3, 4]))
# print(it)

# for element in it:
#     print(element)

# list(map(lambda x: print(x, end=' '), [1, 2, 3, 4]))

# filter
lst = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(lst)