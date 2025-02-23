from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер счета или кредитной карты в зависимости от типа информации.

    :param info: Строка, содержащая имя типа информации и номер счета или карты.
    :return: Строка с замаскированной информацией.
    """
    parts = info.split()
    type_info = ' '.join(parts[:-1])   #Соединяем все части, кроме последней
    number_info = parts[-1]   #Берем последнее слово как номер

    if 'Счет' in type_info:
        return f"{type_info} {get_mask_account(number_info)}"
    else:
        return f"{type_info} {get_mask_card_number(number_info)}"


def get_date(date_str):
    from datetime import datetime

     #Преобразование строки в объект datetime
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
     #Форматирование даты в нужный формат
    return date_obj.strftime("%d.%m.%Y")