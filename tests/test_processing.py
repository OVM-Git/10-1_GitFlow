import unittest
from datetime import datetime
from typing import List, Dict

from src.processing import filter_by_state, sort_by_date


class TestTransactionFunctions(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовых данных."""
        self.test_data = [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]

    def test_filter_by_state_executed(self):
        """Тест фильтрации по state='EXECUTED'."""
        result = filter_by_state(self.test_data, 'EXECUTED')
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertEqual(item['state'], 'EXECUTED')

    def test_filter_by_state_canceled(self):
        """Тест фильтрации по state='CANCELED'."""
        result = filter_by_state(self.test_data, 'CANCELED')
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertEqual(item['state'], 'CANCELED')

    def test_filter_by_state_default(self):
        """Тест фильтрации со значением по умолчанию (EXECUTED)."""
        result = filter_by_state(self.test_data)
        self.assertEqual(len(result), 2)
        for item in result:
            self.assertEqual(item['state'], 'EXECUTED')

    def test_filter_by_state_empty(self):
        """Тест фильтрации пустого списка."""
        result = filter_by_state([])
        self.assertEqual(result, [])

    def test_sort_by_date_descending(self):
        """Тест сортировки по дате (по убыванию)."""
        result = sort_by_date(self.test_data, reverse=True)
        dates = [datetime.fromisoformat(item['date']) for item in result]
        self.assertTrue(all(dates[i] >= dates[i+1] for i in range(len(dates)-1)))

    def test_sort_by_date_ascending(self):
        """Тест сортировки по дате (по возрастанию)."""
        result = sort_by_date(self.test_data, reverse=False)
        dates = [datetime.fromisoformat(item['date']) for item in result]
        self.assertTrue(all(dates[i] <= dates[i+1] for i in range(len(dates)-1)))

    def test_sort_by_date_empty(self):
        """Тест сортировки пустого списка."""
        result = sort_by_date([])
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()