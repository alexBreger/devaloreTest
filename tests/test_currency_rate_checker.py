from src.currency_rate_checker import get_currency_names_rate_lower_than
import pytest

RATE_LOWER_THAN_LIMIT = 10.0


@pytest.fixture()
def mock_currency_data():
    return [{
        "USD": 1.0,
        "EUR": 1.0,
        "NIS": 3.56,
    },
    ]


def test_get_currency_names_rate_lower_than(mock_currency_data):
    assert get_currency_names_rate_lower_than(mock_currency_data, RATE_LOWER_THAN_LIMIT) == {
        "USD": 1.0,
        "EUR": 1.0,
        "NIS": 3.56,
    }

#For the seocnd test maybe that we really got a json file or if the connection succeeded? not sure.