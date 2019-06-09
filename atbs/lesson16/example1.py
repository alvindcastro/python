import copy


def eggs(cheese):
    cheese.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)

ham = ['A',
       'B',
       'C',
       'D']
keso = copy.deepcopy(ham)
keso[1] = 42
print(keso)
print(ham)
