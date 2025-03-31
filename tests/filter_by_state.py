import pytest
from src.processing import filter_by_state

@pytest.fixture
def test_data():
    return [
        {"id": 1, "state": "new"},
        {"id": 2, "state": "pending"},
        {"id": 3, "state": "done"},
        {"id": 4, "state": "new"},
        {"id": 5, "state": "failed"},
        {"id": 6, "state": "pending"},
        {"id": 7, "state": "done"},
        {"id": 8, "state": None},
        {"id": 9},
    ]

@pytest.mark.parametrize("state,expected_ids", [
    ("new", [1, 4]),
    ("pending", [2, 6]),
    ("done", [3, 7]),
    ("failed", [5]),
    ("unknown", []),
    (None, [8]),
])
def test_filter_by_state(test_data, state, expected_ids):
    """Параметризованный тест для различных состояний"""
    result = filter_by_state(test_data, state)
    assert [item["id"] for item in result] == expected_ids

def test_empty_input():
    assert filter_by_state([], "any") == []

def test_missing_state_key(test_data):
    result = filter_by_state(test_data, "new")
    assert all("state" in item for item in result)