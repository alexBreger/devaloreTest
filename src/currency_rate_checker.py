import requests
from settings import constants

# API_KEY should be in different text file or another secured location (best in env?).
# All settings place in a file and read from it.
API_KEY = constants.API_KEY
ENDPOINT = constants.ENDPOINT
BASE_CURRENCY = constants.BASE_CURRENCY
CURRENCY_LOWER_THAN_RATE_LIMIT = constants.CURRENCY_LOWER_THAN_RATE_LIMIT
MIN_RATE = constants.MIN_RATE


def get_currency_names_rate_lower_than(dict_of_currency_rates, currency_rate_limit):
    currency_lower_than_dictionary = {}
    for key, value in dict_of_currency_rates.items():
        if currency_rate_limit > value > MIN_RATE:
            print(f"inserted {key}")
            currency_lower_than_dictionary[key] = value
    if currency_lower_than_dictionary is False:  # Empty dict
        print("No currencies")
    return currency_lower_than_dictionary


# add if statement to check boundaries (0)
def get_api_latest_currency_rate_request(api_key, endpoint, base_currency):
    response = "Not assigned yet"
    try:
        url = f"https://api.apilayer.com/exchangerates_data/{endpoint}?&base={base_currency}"

        payload = {}
        headers = {
            "apikey": api_key
        }

        response = requests.request("GET", url, headers=headers, data=payload)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    finally:
        print(f"Exited with {response.status_code}")

    return response.json()


dict_latest_currency_rates = get_api_latest_currency_rate_request(API_KEY, ENDPOINT, BASE_CURRENCY)
all_currency_names_rate_lower_than = get_currency_names_rate_lower_than(dict_latest_currency_rates["rates"],
                                                                        CURRENCY_LOWER_THAN_RATE_LIMIT)

print(all_currency_names_rate_lower_than)
