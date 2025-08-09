import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(payment: str) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры,
    либо номер счета, оставляя последние 4 цифры

    asoidjKAHDS
    """
    splitted_payment = payment.split()
    payment_type = splitted_payment[:-1]
    payment_digits = splitted_payment[-1]
    if "Счёт" in payment_type:
        return " ".join(payment_type) + " " + get_mask_account(payment_digits)
    else:
        return " ".join(payment_type) + " " + get_mask_card_number(payment_digits)


def get_date(date_str: str) -> str:
    """Функция принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"
    """
    date_obj = datetime.datetime.strptime(date_str.split("T")[0], "%Y-%m-%d")
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
