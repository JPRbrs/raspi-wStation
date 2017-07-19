import requests
import json
from secrets import (
    bus_API,
    portcullis
)


def get_next_bus(stop_id, max_items=3):
    url = 'https://bristol.api.urbanthings.io/api/2.0/rti/stopboard?' +\
          'stopID={}&maxItems={}'.format(
              stop_id,
              max_items)

    headers = {
        'X-Api-Key': bus_API,
        'Accept': 'application/json'
    }

    response = requests.get(url, data=None, headers=headers)

    next_buses = []

    for row in response.json()['data']['stopBoards'][0]['rows']:
        next_buses.append((row['groupID'], row['timeLabel']))

    return next_buses


if __name__ == '__main__':
    get_next_bus(stop_id=portcullis, max_items=1)
