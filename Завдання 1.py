from datetime import datetime

def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        difference = today - given_date
        return difference.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте РРРР-MM-ДД"


date = "2025-04-14"

result = get_days_from_today(date)

print(result)