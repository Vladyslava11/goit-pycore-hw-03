import re


def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує номер телефону до формату +38XXXXXXXXXX.

    Args:
        phone_number: Номер телефону в будь-якому форматі.

    Returns:
        Номер телефону у форматі +38XXXXXXXXXX.
    """
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    if cleaned.startswith("+"):
        return cleaned

    if cleaned.startswith("380"):
        return "+" + cleaned

    return "+38" + cleaned


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print(sanitized_numbers)
