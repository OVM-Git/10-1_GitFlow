import unittest
from datetime import datetime
from unittest.mock import patch

# Тестируемые функции
def mask_account_card(info: str) -> str:
    parts = info.split()
    type_info = ' '.join(parts[:-1])
    number_info = parts[-1]

    if 'Счет' in type_info:
        return f"{type_info} **{number_info[-4:]}"
    else:
        return f"{type_info} {number_info[:4]} {number_info[4:6]}** **** {number_info[-4:]}"


def get_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


class TestMaskAccountCard(unittest.TestCase):
    def test_mask_account(self):
        """Тест маскировки номера счета"""
        self.assertEqual(
            mask_account_card("Счет 1234567890123456"),
            "Счет **3456"
        )

    def test_mask_visa_card(self):
        """Тест маскировки Visa карты"""
        self.assertEqual(
            mask_account_card("Visa Platinum 1234567890123456"),
            "Visa Platinum 1234 56** **** 3456"
        )

    def test_mask_mastercard(self):
        """Тест маскировки Mastercard"""
        self.assertEqual(
            mask_account_card("MasterCard 1234567890123456"),
            "MasterCard 1234 56** **** 3456"
        )

    def test_empty_input(self):
        """Тест пустой строки на входе"""
        with self.assertRaises(IndexError):
            mask_account_card("")


class TestGetDate(unittest.TestCase):
    def test_valid_date(self):
        """Тест корректного преобразования даты"""
        self.assertEqual(
            get_date("2023-04-15T12:30:45.123456"),
            "15.04.2023"
        )

    def test_invalid_date_format(self):
        """Тест некорректного формата даты"""
        with self.assertRaises(ValueError):
            get_date("2023/04/15 12:30:45")

    def test_empty_date(self):
        """Тест пустой строки даты"""
        with self.assertRaises(ValueError):
            get_date("")

    def test_edge_case_date(self):
        """Тест граничного значения даты"""
        self.assertEqual(
            get_date("0001-01-01T00:00:00.000000"),
            "01.01.0001"
        )


if __name__ == '__main__':
    unittest.main()