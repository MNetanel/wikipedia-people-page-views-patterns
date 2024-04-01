import pandas as pd
from pathlib import Path


def timestamp2datetime(timestamp):
    timestamp = str(timestamp)
    year = timestamp[:4]
    month = timestamp[4:6]
    day = timestamp[6:8]
    return f'{year}-{month}-{day}'



def main():
    pass

if __name__ == '__main__':
    main()
