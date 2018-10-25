import requests
import datetime


def load_attempts():
    pages = 10
    for page in range(pages):
        url = 'https://devman.org/api/challenges/solution_attempts/'
        request = requests.get(url, data={'page': 'page'})
        users = request.json()['records']
        for user in users:
            yield {
                'username': user['username'],
                'timestamp': user['timestamp'],
                'timezone': 'Europe/Moscow',
            }


def get_midnighters():
    for user in load_attempts():
        userdatetime = datetime.datetime.fromtimestamp(user['timestamp'])
        usertime = userdatetime.strftime('%H:%M:%S')
        if usertime > '00:00:00' and usertime < '06:00:00':
            print(user['username'])


if __name__ == '__main__':
    get_midnighters()
