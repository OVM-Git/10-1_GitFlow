import unittest

from src.masks import get_mask_account, get_mask_card_number


class TestMaskFunctions(unittest.TestCase):
    def test_get_mask_card_number_valid(self):
        """Тест корректной маскировки номера карты."""
        self.assertEqual(get_mask_card_number("1234567890123456"), "1234 56  3456")
        self.assertEqual(get_mask_card_number("1234 5678 9012 3456"), "1234 56  3456")

    def test_get_mask_card_number_invalid_length(self):
        """Тест вызова исключения при неверной длине номера карты."""
        with self.assertRaises(ValueError):
            get_mask_card_number("123456789012345")  # 15 цифр
        with self.assertRaises(ValueError):
            get_mask_card_number("12345678901234567")  # 17 цифр
        with self.assertRaises(ValueError):
            get_mask_card_number("")  # пустая строка

    def test_get_mask_account_valid(self):
        """Тест корректной маскировки номера счета."""
        self.assertEqual(get_mask_account("1234567890"), "7890")
        self.assertEqual(get_mask_account("0000"), "0000")

    def test_get_mask_account_invalid(self):
        """Тест вызова исключения при невалидном номере счета."""
        with self.assertRaises(ValueError):
            get_mask_account("1234abc567890")  # содержит буквы
        with self.assertRaises(ValueError):
            get_mask_account("")  # пустая строка
        with self.assertRaises(ValueError):
            get_mask_account(1234567890)  # не строка


if __name__ == "__main__":
    unittest.main()