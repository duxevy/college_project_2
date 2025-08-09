def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры.

    Returns: masked card number
    9120938
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта, оставляя только последние 4 цифры.

    Return: masked account number
    """

    return f"**{account_number[-4:]}!!!"
