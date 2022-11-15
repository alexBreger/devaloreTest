from src.currency_rate_checker import get_currency_names_rate_lower_than
import pytest
from settings import constants

RATE_LOWER_THAN_LIMIT = constants.CURRENCY_LOWER_THAN_RATE_LIMIT


@pytest.fixture()
def mock_currency_data():
    return [{
        "USD": 10,
        "EUR": 9,
        "NIS": -1  # a bug was found
    },
    ]


def test_rate_higher_than_zero():
    assert RATE_LOWER_THAN_LIMIT > 0


def test_get_currency_names_rate_lower_than(mock_currency_data):
    assert get_currency_names_rate_lower_than(mock_currency_data[0], RATE_LOWER_THAN_LIMIT) == {"EUR": 9}






