from datetime import datetime, date, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """
    Повертає список користувачів з днями народження на найближчі 7 днів.

    Args:
        users: Список словників з ключами 'name' та 'birthday'.

    Returns:
        Список словників з іменами та датами привітань.
    """
    today = datetime.today().date()
    end_day = today + timedelta(days=7)
    result = []

    for user in users:
        bday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        bday_this_year = bday.replace(year=today.year)

        if bday_this_year < today:
            bday_this_year = bday_this_year.replace(year=today.year + 1)

        if today <= bday_this_year <= end_day:
            congrats_day = bday_this_year

            # 5 = Saturday, 6 = Sunday
            if congrats_day.weekday() == 5:
                congrats_day = congrats_day + timedelta(days=2)
            elif congrats_day.weekday() == 6:
                congrats_day = congrats_day + timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congrats_day.strftime("%Y.%m.%d")
            })

    return result


if __name__ == "__main__":
    users = [
        {"name": "Vladyslava Slipchenko", "birthday": "1994.02.11"},
        {"name": "Natalia Slipchenko", "birthday": "1973.02.09"},
        {"name": "Mykola Kosovsky", "birthday": "1997.02.10"}
    ]

    print(get_upcoming_birthdays(users))
