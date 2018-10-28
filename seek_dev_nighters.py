import requests
import datetime
from datetime import datetime
import pytz


def load_attempts():
    pages = 1
    page = 1
    url = 'https://devman.org/api/challenges/solution_attempts/'
    while page <= pages:
        attempts_data = requests.get(url, data={'page': 'page'})
        attempts_data_formatted = attempts_data.json()
        attempts = attempts_data_formatted['records']
        pages = attempts_data_formatted['number_of_pages']
        page += 1
        for attempt in attempts:
            yield {
                'username': attempt['username'],
                'timestamp': attempt['timestamp'],
                'timezone': attempt['timezone'],
            }


def get_midnighters(load_attempts):
    midnighters = []
    for attempt in load_attempts:
        attempts_dt = datetime.fromtimestamp(attempt['timestamp'],
                                             pytz.timezone(attempt['timezone'])
                                             )
        hour = attempts_dt.hour
        if hour >= 0 and hour < 6 and attempt['username'] not in midnighters:
            midnighters.append(attempt['username'])
    return midnighters


if __name__ == '__main__':
    midnighters = get_midnighters(load_attempts())
    if midnighters:
        print('Night Owl students on DevMan:')
        for username in midnighters:
            print(username)
