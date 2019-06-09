import random

print('Hello. What is your name?')
name = input()
secret_number = random.randint(1, 20)
print('Well ' + name + ', I am thinking of a number betwwen 1 and 20. Take a guess...')

for guesses in range(1, 7):
    print('Take a guess...')
    guess = int(input())
    if guess < secret_number:
        print('Guess is too low...')
    elif guess > secret_number:
        print('Guess is too high...')
    else:
        break

if guess == secret_number:
    print('Good job, ' + name + '! You guessed my number in ' + str(guesses) + ' guesses')
else:
    print('Nope, the number I was thinking of is ' + str(secret_number))
