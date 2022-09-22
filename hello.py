# value = None
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello world' # \n переход на новую строку

# print(s) # Вывод строки
# print(a, '-',b, '-', s)
# print('{1} - {2} - {0}'.format(a,b,s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1, 2, 4.5, True]
# print(list)

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, ' + ' , b, ' = ', a+b)
# # print('{} {}'. format(a, b))
# # print(f'{a} {b}')

# a = 1.3123321
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a += 5
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print (a==b)

# a = [1,2]
# b = [1,2]
# print(a == b)

# a = 1 < 3 < 5
# print(a)

# func = 1
# T = 4
# x = 123
# print(func<T>(x)) # Тоже тройное неравенство

# func = 1
# T = 4
# x = 2

# print(func<T>(x))


# f = 1 > 2 or 4 < 6
# если хотя бы одно значение верно то будет True
# print(f)

# f = [1,2,3,4]
# print(f)
# print(2 in f)  # Будет True так как 2 сожержится в списке, если написать print(not 2 in f) то будет False


# is_odd = f[0] % 2 == 0
# print(is_odd)

# is_odd = not f[0] % 2     # ТОже самое что и предыдущее только более Pythonовкое написание
# print(is_odd)

# Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#         print('Привет, ', username)

# Управляющие конструкции
# while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции
# while-else

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции
# for

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:          # Тоже самое только через список
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(10):       # Это тоже самое что и прошлое только без переменной r
#     print(i)

# for i in range(1, 5):       # С указанием диапазона
#     print(i)

for i in range(1, 10, 2):       # не четные числа в диапазоне от 1 до 9 так как n-1, а не до 10
    print(i)