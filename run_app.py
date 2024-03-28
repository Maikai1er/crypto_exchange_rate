from datetime import time

from write_to_file import write_to_file


def run_app():
    while True:
        write_to_file(currency='BTCUSDT')
