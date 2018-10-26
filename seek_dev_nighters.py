import requests
import datetime
from datetime import datetime
import pytz


def load_attempts():
    pages = 1
    page = 1
    url = 'https://devman.org/api/challenges/solution_attempts/'
    while page <= pages:
        get_att_data = requests.get(url, data={'page': 'page'})
        att_data_formatted = get_att_data.json()
        attempts = att_data_formatted['records']
        pages = att_data_formatted['number_of_pages']
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
        att_dt = datetime.fromtimestamp(attempt['timestamp'])
        att_dt_utc = pytz.utc.localize(att_dt)
        tmz = pytz.timezone(attempt['timezone'])
        att_dt_local = att_dt_utc.astimezone(tmz)
        hour = att_dt_local.hour
        if hour >= 0 and hour < 6 and attempt['username'] not in midnighters:
            midnighters.append(attempt['username'])
    return midnighters


if __name__ == '__main__':
    print(get_midnighters(load_attempts()))
