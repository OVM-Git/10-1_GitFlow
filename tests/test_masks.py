import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_valid():
    """Тест корректного маскирования номера карты."""
    assert get_mask_card_number("1234567890123456") == "1234 56  3456"
    assert get_mask_card_number("1234 5678 9012 3456") == "1234 56  3456"

def test_get_mask_card_number_invalid_length():
    """Тест обработки номера карты с некорректной длиной."""
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number("123456789012345")  # 15 цифр
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number("12345678901234567")  # 17 цифр

def test_get_mask_account_valid():
    """Тест корректного маскирования номера счета."""
    assert get_mask_account("1234567890") == "7890"
    assert get_mask_account("987654") == "7654"

def test_get_mask_account_invalid_input():
    """Тест обработки невалидного ввода номера счета."""
    with pytest.raises(ValueError, match="Номер счета должен быть строкой, содержащей только цифры."):
        get_mask_account("1234abc5678")  # содержит буквы
    with pytest.raises(ValueError, match="Номер счета должен быть строкой, содержащей только цифры."):
        get_mask_account(1234567890)  # не строка
    with pytest.raises(ValueError, match="Номер счета должен быть строкой, содержащей только цифры."):
        get_mask_account("")  # пустая строка