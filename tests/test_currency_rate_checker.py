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


# write test for get_currency_names_rate_lower_than. Write hard coded json to check 9 and 10
# (9 lower than 10 and 10 higher than 10) higher shouldn't get through and lower should
# Run test with, 5 and get usd (usd = 9) run test with 10 and get error that we don't need above 10.


def test_rate_higher_than_zero():
    assert RATE_LOWER_THAN_LIMIT > 0


def test_get_currency_names_rate_lower_than(mock_currency_data):
    assert get_currency_names_rate_lower_than(mock_currency_data[0], RATE_LOWER_THAN_LIMIT) == {"EUR": 9}






