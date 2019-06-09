import random


def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'No'
    elif answer_number == 5:
        return 'Try again'
    elif answer_number == 6:
        return 'Ask again later'
    elif answer_number == 7:
        return 'How about no'
    elif answer_number == 8:
        return 'Yes... surprisingly'
    elif answer_number == 9:
        return 'NOOOOOONOOOOOOOOOYES'


print('Think of a yes/no question, and press enter')
input()

print(get_answer(random.randint(1, 9)))
