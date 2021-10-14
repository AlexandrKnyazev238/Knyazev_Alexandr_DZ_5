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

rezult = (i for i in zip_longest(tutors, klasses))

print(type(rezult))
print(next(rezult))
print(*islice(rezult, 7))
# print(next(rezult))
# print(next(rezult))
# print(next(rezult))
# print(next(rezult))
# print(next(rezult))
# print(next(rezult))
# print(next(rezult))
# print(next(rezult))
