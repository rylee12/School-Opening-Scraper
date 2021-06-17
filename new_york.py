import logging
import requests
import pandas as pd
import os
from datetime import datetime, date

def main():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    download_csv()
    logging.info("Received New York Data", exc_info=False);
    copy_to_new_csv()
    logging.info("Wrote New York Data", exc_info=False);

def download_csv():
    url = "https://docs.google.com/spreadsheets/d/1U0FSbm77qXB4shssE66EFgp-I8Ia_I6_xYrotKk3Zqg/export?format=xlsx"
    originalFile = requests.get(url)
    open('temp/NYOriginal.xlsx', 'wb').write(originalFile.content)

def copy_to_new_csv():
    df = pd.read_excel('temp/NYOriginal.xlsx', sheet_name=None)
    for key in df.keys():
        df[key].to_csv('temp/{}.csv'.format(key))

    li=[]
    for filename in os.listdir("temp/"):
        if filename.startswith("Wave"):
            tmp = pd.read_csv("temp/"+filename, index_col=None, header=0)
            li.append(tmp)

    df = pd.concat(li, axis=0, ignore_index=True)
    df.to_csv('out/NY_' + datetime.now().strftime('%Y%m%d') + '.csv', index=False)

#main()
