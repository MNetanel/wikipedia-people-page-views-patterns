from dotenv import load_dotenv
import requests
import os
from pathlib import Path
from tqdm import tqdm
import pandas as pd
import time

load_dotenv()


def fetch_pageviews_for_article(article: str):
    base_url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/'

    params = {
        'project': 'en.wikipedia.org',
        'access': 'all-access',
        'agent': 'user',
        'article': article,
        'granularity': 'daily',
        'start': '20000101',
        'end': '20240131'
    }

    request_url = base_url + '/'.join(params.values())
    response = requests.get(request_url,
                            headers={'User-Agent': os.getenv('EMAIL')})
    if response.status_code != 200:
        raise Exception('Response unsuccessful')
    return response

def get_pageviews_data(articles_df: pd.DataFrame, out_dir: Path):
    t = tqdm(articles_df.href)
    for href in t:
        article = href[6:]
        t.set_postfix_str(article)  # display the current article in progressbar
        filepath = str(out_dir / f'{article}.csv')
        if not Path(filepath).exists():
            response = fetch_pageviews_for_article(article)
            df = pd.DataFrame(response.json()['items'])[['article', 'timestamp', 'views']]
            df.to_csv(filepath)
            time.sleep(0.1)  # prevent query blockage
            
def fix_broken_files(dir: Path):
    broken_files = [f for f in dir.glob('*[!.csv]')]
    t = tqdm(broken_files)
    for file in t:
        article = file.name
        t.set_postfix_str(article)
        out_filepath = str(dir / f'{article}.csv')
        response = fetch_pageviews_for_article(article)
        df = pd.DataFrame(response.json()['items'])[['article', 'timestamp', 'views']]
        df.to_csv(out_filepath)
        os.remove(file)
        time.sleep(0.1)  # prevent query blockage

def main():
    data_dir = Path(__file__).parents[2] / 'data'
    top100_filepath = data_dir / 'top100_lists' / 'top100.csv'
    pageviews_dir = data_dir / 'pageviews'
    fix_broken_files(pageviews_dir)
    # top100 = pd.read_csv(top100_filepath)
    
    # get_pageviews_data(top100, out_dir=pageviews_dir)

if __name__ == '__main__':
    main()