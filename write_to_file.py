from get_exchange_rate import get_exchange_rate
from get_time import get_current_time
import time


def write_to_file(currency):
    data = get_exchange_rate(currency)
    full_current_time = get_current_time()
    current_date = full_current_time.strftime('%m-%d-%Y')
    current_time = full_current_time.strftime('%H-%M-%S')
    try:
        with open(current_date, 'a') as file:
            file.write(f'\n{current_time}: {data}')
    except FileNotFoundError:
        print('File not found')
        return
