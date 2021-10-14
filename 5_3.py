# Task_3

from itertools import islice, zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
for el in tutors:
    if len(tutors) > len(klasses):
        klasses.append(None)

result = (i for i in zip_longest(tutors, klasses))

print(type(result))
print(next(result))
print(*islice(result, 7))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
