# Task 1

def odd_nums(num):
    for num in range(1, num + 1, 2):
        yield num


for i in odd_nums(int(input('Перед Вами генератор нечетных чисел от 1 до n (включительно),'
                            ' введите пожалуйста число n: '))):
    print(i)

# def odd_nums(n):
#    for odd_num in range(1, n + 1, 2):
#        yield odd_num


# odd_to_15 = odd_nums(15)
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
