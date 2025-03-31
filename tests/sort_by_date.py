import pytest
from src.processing import sort_by_date


@pytest.fixture
def test_data():
    return [
        {"id": 1, "date": "2023-05-15"},
        {"id": 2, "date": "2023-01-20"},
        {"id": 3, "date": "2023-08-10"},
        {"id": 4, "date": "2022-12-31"},
        {"id": 5, "date": "2023-05-15"},  # Та же дата, что у id=1
        {"id": 6, "date": "2024-01-01"},
    ]


@pytest.fixture
def test_data_various_formats():
    return [
        {"id": 1, "date": "15.05.2023"},
        {"id": 2, "date": "2023/01/20"},
        {"id": 3, "date": "Aug 10, 2023"},
        {"id": 4, "date": "31-12-2022"},
        {"id": 5, "date": "20230515"},
    ]


@pytest.mark.parametrize("ascending,expected_ids", [
    (True, [4, 2, 1, 5, 3, 6]),  # По возрастанию
    (False, [6, 3, 1, 5, 2, 4]),  # По убыванию
])
def test_sort_order(test_data, ascending, expected_ids):
    """Параметризованный тест для проверки порядка сортировки"""
    result = sort_by_date(test_data, ascending=ascending)
    assert [item["id"] for item in result] == expected_ids


def test_duplicate_dates_order(test_data):
    """Проверка порядка элементов с одинаковыми датами"""
    result = sort_by_date(test_data, ascending=True)
    ids = [item["id"] for item in result]

    # Проверяем, что id=1 идет перед id=5 (исходный порядок сохранен)
    assert ids.index(1) < ids.index(5)


def test_various_date_formats(test_data_various_formats):
    """Проверка работы с различными форматами дат"""
    result = sort_by_date(test_data_various_formats, ascending=True)
    assert [item["id"] for item in result] == [4, 2, 1, 3, 5]


def test_empty_list():
    """Проверка работы с пустым списком"""
    assert sort_by_date([], ascending=True) == []


def test_missing_date_key(test_data):
    """Проверка обработки элементов без ключа date"""
    test_data.append({"id": 7})  # Элемент без даты
    with pytest.raises(KeyError):
        sort_by_date(test_data, ascending=True)


@pytest.mark.parametrize("invalid_data", [
    [{"id": 1, "date": "invalid-date"}],
    [{"id": 1, "date": "2023-13-01"}],  # Несуществующая дата
    [{"id": 1, "date": None}],  # None вместо даты
])
def test_invalid_date_formats(invalid_data):
    """Параметризованный тест для некорректных форматов дат"""
    with pytest.raises(ValueError):
        sort_by_date(invalid_data, ascending=True)