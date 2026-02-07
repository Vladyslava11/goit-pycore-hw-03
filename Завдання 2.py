import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Генерує випадкові унікальні числа для лотерейного квитка.

    Args:
        min: Мінімальне можливе число (>= 1).
        max: Максимальне можливе число (<= 1000).
        quantity: Кількість чисел для генерації.

    Returns:
        Список унікальних випадкових чисел, відсортованих за зростанням.
        Порожній список, якщо параметри невалідні.
    """
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


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print(lottery_numbers)
