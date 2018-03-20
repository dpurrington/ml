import os
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np
import zipfile

STOCK_URL = "https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs/downloads/Data.zip/3"
STOCK_PATH = os.path.join("datasets", "stock", "Stocks")
print(STOCK_URL)

def fetch_data(stock_url=STOCK_URL, stock_path=STOCK_PATH):
    if not os.path.isdir(stock_path):
        os.makedirs(stock_path)
    zip_path = os.path.join(stock_path, "stock.zip")
    urllib.request.urlretrieve(stock_url, zip_path)
    zip = zipfile.ZipFile(zip_path, 'r')
    zip.extractall(path=stock_path)
    zip.close()

def load_data(stock_path=STOCK_PATH):
    csv_path = os.path.join(stock_path, "cmpr.us.txt")
    return pd.read_csv(csv_path)
