import pytest
from datetime import datetime
from typing import List, Dict
from src.processing import filter_by_state, sort_by_date  # Замените your_module на имя вашего модуля


@pytest.fixture
def sample_data() -> List[Dict]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


def test_filter_by_state_executed(sample_data: List[Dict]):
    result = filter_by_state(sample_data, 'EXECUTED')
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)


def test_filter_by_state_canceled(sample_data: List[Dict]):
    result = filter_by_state(sample_data, 'CANCELED')
    assert len(result) == 2
    assert all(item['state'] == 'CANCELED' for item in result)


def test_filter_by_state_default(sample_data: List[Dict]):
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert all(item['state'] == 'EXECUTED' for item in result)


def test_filter_by_state_empty_result(sample_data: List[Dict]):
    result = filter_by_state(sample_data, 'PENDING')
    assert len(result) == 0


def test_sort_by_date_descending(sample_data: List[Dict]):
    result = sort_by_date(sample_data, reverse=True)
    dates = [datetime.fromisoformat(item['date']) for item in result]
    assert dates == sorted(dates, reverse=True)
    assert result[0]['id'] == 41428829
    assert result[-1]['id'] == 939719570


def test_sort_by_date_ascending(sample_data: List[Dict]):
    result = sort_by_date(sample_data, reverse=False)
    dates = [datetime.fromisoformat(item['date']) for item in result]
    assert dates == sorted(dates, reverse=False)
    assert result[0]['id'] == 939719570
    assert result[-1]['id'] == 41428829


def test_sort_by_date_empty_list():
    assert sort_by_date([]) == []