import argparse
import os
from urllib.parse import urlparse

import requests

from bitlink import get_bitlink_clicks, get_or_create_bitlink, is_bitlink

API_TOKEN = os.environ['API_TOKEN']


cli_parser = argparse.ArgumentParser(
    description='CLI utility for working with the bitly link shortener service using their API'
)
cli_parser.add_argument('url', help='A long url to be shortened or bitlink to get metrics')
cli_args = cli_parser.parse_args()


input_url = cli_args.url
if not urlparse(input_url).scheme:
    print('Ссылка введена неверно: Используйте http:// или https://')
    exit(1)

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
