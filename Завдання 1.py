from datetime import datetime


def get_days_from_today(date: str) -> int | str:
    """
    Обчислює кількість днів між заданою датою та сьогоднішнім днем.

    Args:
        date: Рядок дати у форматі 'РРРР-ММ-ДД'.

    Returns:
        Кількість днів як ціле число, або рядок з повідомленням про помилку.
    """
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        difference = today - given_date
        return difference.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте РРРР-MM-ДД"


if __name__ == "__main__":
    date = "2025-04-14"
    result = get_days_from_today(date)
    print(result)
