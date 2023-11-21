import requests
import traceback
from requests.exceptions import ConnectTimeout


# timeout=None      ->   Wait forever
# timeout=(connect_timeout, read_timeout)
def timeout():
    try:
        r = requests.get('https://github.com/', timeout=0.001)
        # r = requests.get('https://github.com', timeout=(3.05, 27))
        # r = requests.get('https://github.com', timeout=None)
    except ConnectTimeout:
        traceback.print_exc(limit=1)
        print('Request has timed out')

    # Returns:
    # Request has timed out


timeout()
