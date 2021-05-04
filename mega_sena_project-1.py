from random import randint
from time import sleep
print('=' * 21)
print('= Mega-Sena Numbers =')
print('=' * 21)
numbers = []
while len(numbers) != 6:
    number = randint(1, 60)
    if number not in numbers:
        print(f'{number}' , end=' → ')
        sleep(0.1)
        numbers.append(number)
numbers.sort()
print(numbers)
