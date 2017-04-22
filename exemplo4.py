import os
import requests
from multiprocessing.pool import ThreadPool as Pool


urls = (
    'http://www.americanas.com',
    'http://www.submarino.com',
    'http://www.shoptime.com',
    'http://www.soubarato.com',
)


def get_and_print(url):
    response = requests.get(url)
    print(response.text)


pool = Pool(processes=os.cpu_count())
pool.map(get_and_print, urls)
