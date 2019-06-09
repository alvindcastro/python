# spam = ['h', 'e', 'l', 'L', 'H']
spam = ['a', 'z', 'A', 'Z']
spam.sort()
spam.sort(key=str.lower)
print(spam)

print(spam.index('a'))

spam.append('o')

print(spam)

spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
