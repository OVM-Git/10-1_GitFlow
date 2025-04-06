import re

def mask_account_card(input_info: str) -> str:
    """
    Маскирует номер счета или карты в строке, оставляя только последние 4 цифры видимыми.

    :param input_info: Строка, содержащая информацию о счете или карте.
    :return: Строка с замаскированным номером счета или карты.
    """
    # Ищем в строке последовательность из 16 цифр (номер карты) или цифр любой длины (номер счета)
    match = re.search(r'\d{16}|\d+', input_info)

    if match:
        number = match.group(0)  # Получаем найденный номер
        start = match.start()  # Получаем индекс начала номера в строке
        end = match.end()  # Получаем индекс конца номера в строке

        if len(number) == 16:
            masked_number = number[:4] + ' ' + number[4:6] + '** **** ' + number[12:]
        else:
            masked_number = "**" + number[-4:] if len(number) > 4 else "**" + number

        return input_info[:start] + masked_number + input_info[end:]
    else:
        return input_info


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя только последние 4 цифры видимыми.

    :param card_number: Номер кредитной карты (строка), состоящий из 16 цифр.
    :raises ValueError: Если длина номера карты не равна 16.
    :return: Строка с замаскированным номером карты.
    """
    card_number = card_number.replace(' ', '')
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")

    masked_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[12:16]
    return masked_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры видимыми.

    :param account_number: Номер счета (строка), содержащий только цифры.
    :raises ValueError: Если номер счета не является строкой с цифрами.
    :return: Строка с замаскированным номером счета.
    """
    if isinstance(account_number, str) and account_number.isdigit():
        masked_part = account_number[-4:]

        return f"**{masked_part}"
    else:
        raise ValueError("Номер счета должен быть строкой, содержащей только цифры.")



'''
def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя только последние 4 цифры видимыми.

    :param card_number: Номер кредитной карты (строка), состоящий из 16 цифр.
    :raises ValueError: Если длина номера карты не равна 16.
    :return: Строка с замаскированным номером карты.
    """
    card_number = card_number.replace(' ', '')
    if len(card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")

    masked_number = card_number[:4] + ' ' + card_number[4:6] + '  ' + card_number[12:16]
    return masked_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры видимыми.

    :param account_number: Номер счета (строка), содержащий только цифры.
    :raises ValueError: Если номер счета не является строкой с цифрами.
    :return: Строка с замаскированным номером счета.
    """
    if isinstance(account_number, str) and account_number.isdigit():
        masked_part = account_number[-4:]
        return f"{masked_part}"
    else:
        raise ValueError("Номер счета должен быть строкой, содержащей только цифры.")
'''