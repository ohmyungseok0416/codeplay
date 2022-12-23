import random

def sorting(length):
    numbers = []
    num = 0
    while len(numbers) < length:
        num = random.randint(1, 1000)
        if num in numbers:
            continue
        else:
            numbers.append(num)
    print (numbers)
    shift = 0
    count = 0
    while True:
        shift = 0
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] =numbers[i + 1], numbers[i]
                shift += 1
                count += 1
        if shift == 0:
            break
    print(numbers)
    print(f"{count}번의 반복")
number = int(input("몇개의 숫자를 만득시겟듭닏까"))
sorting(number)