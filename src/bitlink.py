import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

load_dotenv()

API_PATH = 'https://api-ssl.bitly.com/v4'


def clear_scheme_in_url(absolute_url):
    sliced_url = urlparse(absolute_url)
    cleaned_url = f'{sliced_url.netloc}{sliced_url.path}'
    return cleaned_url


def is_bitlink(token, url):
    cleaned_url = clear_scheme_in_url(url)

    api_url = f'{API_PATH}/bitlinks/{cleaned_url}'

    request_headers = {
        "Authorization": f'Bearer {token}',
    }

    response = requests.get(api_url, headers=request_headers)

    return response.ok


def get_bitlink_clicks(token, bitlink):
    cleaned_url = clear_scheme_in_url(bitlink)

    api_url = f'{API_PATH}/bitlinks/{cleaned_url}/clicks/summary'

    request_headers = {
        "Authorization": f'Bearer {token}',
    }
    request_parameters = {
        "unit": "month",
        "units": -1,
    }

    response = requests.get(
        api_url,
        headers=request_headers,
        params=request_parameters,
    )
    response.raise_for_status()

    return response.json().get('total_clicks')


def get_or_create_bitlink(token, long_url):
    api_url = f'{API_PATH}/shorten'

    request_headers = {
        "Authorization": f'Bearer {token}',
    }
    request_body = {
        "long_url": long_url,
    }

    response = requests.post(api_url,
                             headers=request_headers,
                             json=request_body)
    response.raise_for_status()

    return response.json().get('link')


if __name__ == "__main__":
    API_TOKEN = os.environ['API_TOKEN']

    while True:
        input_url = input('Your Link (absolute url):')
        if urlparse(input_url).scheme:
            break
        print('Ссылка введена неверно: Используйте http:// или https://')

    if is_bitlink(API_TOKEN, input_url):
        try:
            bitlink_clicks = get_bitlink_clicks(API_TOKEN, input_url)
            print("Количество кликов: ", bitlink_clicks)
        except requests.exceptions.HTTPError as error:
            print('Что-то пошло не так. Ошибка: ', error)
    else:
        try:
            bitlink = get_or_create_bitlink(API_TOKEN, input_url)
            print('Битлинк', bitlink)
        except requests.exceptions.HTTPError as error:
            print('Что-то пошло не так. Ошибка: ', error)
