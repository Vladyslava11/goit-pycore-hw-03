import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []
    
    if quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = set()

    while len(numbers) < quantity:
        num = random.randint(min, max)
        numbers.add(num)

    result = list(numbers)
    result.sort()

    return result


lottery_numbers = get_numbers_ticket(1, 49, 6)
print(lottery_numbers)