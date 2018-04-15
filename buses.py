import requests
from secrets import (
    bus_API,
)


def get_next_bus(stop_id, max_items=1):
    url = 'https://bristol.api.urbanthings.io/api/2.0/rti/stopboard?' +\
          'stopID={}&maxItems={}'.format(
              stop_id,
              max_items)

    headers = {
        'X-Api-Key': bus_API,
        'Accept': 'application/json'
    }

    response = requests.get(url, data=None, headers=headers)
    response_rows = response.json()['data']['stopBoards'][0]['rows']

    # next_buses = {
    #     'number': row['groupID'],
    #     'time': row['timeLabel'] for row in response_rows
    #     }

    return response_rows
