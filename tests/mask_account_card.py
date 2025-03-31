import pytest

from your_module import mask_account_card  # Замените your_module на имя вашего файла

# Параметризованные тесты для разных типов карт и счетов
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("1234567890123456", "1234XXXXXXXXXXXX3456"),  # Visa/Mastercard
        ("341122334455667", "341XXXXXXXXXXXXX667"),  # Amex
        ("6011000000000000", "6011XXXXXXXXXXXX0000"),  # Discover
        ("4141111122223333", "4141XXXXXXXXXXXX3333"),  # Visa
        ("5123456789012345", "5123XXXXXXXXXXXX2345"),  # Mastercard
        ("378282246310005", "378XXXXXXXXXXXXX005"), # Amex
        ("4444444444444444", "4444XXXXXXXXXXXX4444"),  # Другая карта
        ("1234567890", "123XXXXX90"),  # Счет (10 цифр)
        ("9876543210", "987XXXXX10"),  # Счет (10 цифр)
        ("112233445566778899", "112233445566778899"), # Некорректная длина карты/счета - не маскируется
    ],
)
def test_mask_account_card_valid_input(input_string, expected_output):
    """Тестирует функцию с корректными данными различных типов карт и счетов."""
    assert mask_account_card(input_string) == expected_output


# Тесты для обработки некорректных входных данных
@pytest.mark.parametrize(
    "invalid_input",
    [
        "",  # Пустая строка
        None,  # None
        "abc123xyz",  # Строка с нецифровыми символами
        "123",  # Слишком короткая строка
        "123456789012345678901234567890",  # Слишком длинная строка
    ],
)
def test_mask_account_card_invalid_input(invalid_input):
    """Тестирует функцию с некорректными данными и проверяет, что она не падает."""
    with pytest.raises(ValueError): # Или другой тип исключения, который выбрасывает ваша функция.
        mask_account_card(invalid_input)

# Тест на обработку чисел, переданных как int (если ваша функция предполагает строковый ввод)
def test_mask_account_card_integer_input():
    """Тестирует функцию с целым числом в качестве входных данных (если ожидается строка)."""
    with pytest.raises(TypeError):  # Ожидаем ошибку типа, если функция принимает только строки
        mask_account_card(1234567890123456)


# Пример теста, если функция должна возвращать None или пустую строку для некорректных данных
def test_mask_account_card_invalid_input_returns_none():
    """Тестирует, что функция возвращает None для некорректных данных (альтернативное поведение)."""
    assert mask_account_card("invalid_data") is None  # Или assert mask_account_card("invalid_data") == ""
