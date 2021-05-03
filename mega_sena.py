from random import randint
from time import sleep
print('=' * 21)
print('= Mega-Sena Numbers =')
print('=' * 21)
numbers = []
for c in range(0, 6):
    number = randint(1, 60)
    if number not in numbers:
        print(number)
        numbers.append(number)
    sleep(1)
numbers.sort()
print(numbers)
