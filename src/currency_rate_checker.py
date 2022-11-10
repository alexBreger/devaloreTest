import requests


# for some reason it didn't let me connect to the API sayong API access key is invalid although I copy pasted it and followed documentation.
# I used documentation examples to try and make this method.
def get_currency_names_rate_lower_than(json_of_currency_rates, currency_rate_limit):
    currency_lower_than = currency_rate_limit
    currency_lower_than_dictionary = {}
    for key, value in json_of_currency_rates:
        if value < currency_lower_than:
            currency_lower_than_dictionary[key] = value
    return currency_lower_than_dictionary


def get_api_latest_currency_rate_request(api_key, endpoint, base_currency):
    response = "Not assigned yet"
    try:
        response = requests.get(
            f"https://api.exchangeratesapi.io/v1/{endpoint}?access_key={api_key}&base={base_currency}")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    finally:
        print(f"Exited with {response.status_code}")
    return response.json()


# API_KEY should be in different text file or another secured location (best in env?).
API_KEY = "7QtMIOKDXbo8x3h8gqbPq613UcRAZIIv"
ENDPOINT = "latest"
BASE_CURRENCY = "USD"
CURRENCY_LOWER_THAN_RATE_LIMIT = 10.0

json_latest_currency_rates = get_api_latest_currency_rate_request(API_KEY, ENDPOINT, BASE_CURRENCY)
all_currency_names_rate_lower_than = get_currency_names_rate_lower_than(json_latest_currency_rates["rates"], CURRENCY_LOWER_THAN_RATE_LIMIT)

print(all_currency_names_rate_lower_than)
