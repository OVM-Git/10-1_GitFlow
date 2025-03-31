import unittest
from datetime import datetime
from  src. widget import get_date  # Импортируем тестируемую функцию


class TestGetDateFunction(unittest.TestCase):
    """Тесты для функции get_date модуля widget"""

    def test_standard_date_formats(self):
        """Проверка стандартных форматов дат"""
        test_cases = [
            # (входная строка, ожидаемый результат)
            ("2023-05-15", datetime(2023, 5, 15)),
            ("15.05.2023", datetime(2023, 5, 15)),
            ("05/15/2023", datetime(2023, 5, 15)),
            ("20230515", datetime(2023, 5, 15)),
            ("15-May-2023", datetime(2023, 5, 15)),
            ("May 15, 2023", datetime(2023, 5, 15)),
        ]

        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(get_date(input_str), expected)

    def test_edge_cases(self):
        """Проверка граничных случаев"""
        # Проверка високосных годов
        self.assertEqual(get_date("29.02.2020"), datetime(2020, 2, 29))

        # Проверка минимальной и максимальной дат
        self.assertEqual(get_date("01.01.0001"), datetime(1, 1, 1))
        self.assertEqual(get_date("31.12.9999"), datetime(9999, 12, 31))

        # Проверка разных разделителей
        self.assertEqual(get_date("2023 05 15"), datetime(2023, 5, 15))
        self.assertEqual(get_date("2023_05_15"), datetime(2023, 5, 15))

    def test_non_standard_formats(self):
        """Проверка нестандартных форматов"""
        test_cases = [
            ("15th May 2023", datetime(2023, 5, 15)),
            ("2023 May 15", datetime(2023, 5, 15)),
            ("15-May-23", datetime(2023, 5, 15)),
            ("5/15/23", datetime(2023, 5, 15)),
            ("15052023", datetime(2023, 5, 15)),
            ("2023-5-15", datetime(2023, 5, 15)),
        ]

        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(get_date(input_str), expected)

    def test_invalid_inputs(self):
        """Проверка обработки некорректных входных данных"""
        invalid_inputs = [
            "",  # пустая строка
            "not a date",  # текст без даты
            "32.01.2023",  # несуществующая дата
            "31.04.2023",  # апрель не имеет 31 дня
            "2023-13-01",  # несуществующий месяц
            "2023-00-15",  # нулевой месяц
            "2023-05-00",  # нулевой день
            "99999-05-15",  # год за пределами допустимого
            "15/15/2023",  # несуществующий месяц
            "May 32, 2023",  # несуществующий день
        ]

        for input_str in invalid_inputs:
            with self.subTest(input_str=input_str):
                with self.assertRaises(ValueError):
                    get_date(input_str)

    def test_partial_dates(self):
        """Проверка строк с частичной информацией о дате"""
        # Ожидается, что функция вернет None или выбросит исключение
        # в зависимости от требований (нужно уточнить спецификацию)
        test_cases = [
            "May 2023",  # только месяц и год
            "2023",  # только год
            "15 May",  # только день и месяц
        ]

        for input_str in test_cases:
            with self.subTest(input_str=input_str):
                with self.assertRaises(ValueError):
                    get_date(input_str)

    def test_strings_with_extra_text(self):
        """Проверка строк с дополнительным текстом вокруг даты"""
        test_cases = [
            ("Date: 2023-05-15", datetime(2023, 5, 15)),
            ("Report from 15.05.2023", datetime(2023, 5, 15)),
            ("15-May-2023 (final)", datetime(2023, 5, 15)),
            ("Created on May 15, 2023 at 14:30", datetime(2023, 5, 15)),
        ]

        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(get_date(input_str), expected)


if __name__ == '__main__':
    unittest.main()


