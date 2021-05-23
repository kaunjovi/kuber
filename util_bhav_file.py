import pandas as pd 
import urllib.request
from urllib.error import HTTPError, URLError
from socket import timeout
import shutil
import calendar


# Download text from url and save it in a local file. 
# Raise error if you cant. Most likely becuase the url was not existent. 
# Can be moved to util actually
def download_from_url_to_file(url_to_download_data_from, file_to_download_data_at) : 
    try:
        with urllib.request.urlopen(url_to_download_data_from, timeout=10) as response, open(file_to_download_data_at, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except timeout:
        # logging.exception(f'Could not download data from {url_to_download_data_from}')
        raise


def prep_raw_bhv_data_for_analysis ( df ) : 
    df.rename(columns=lambda x: x.strip(), inplace=True)

    ## DELIV_PER has some '-' in it. Fix them. Fix the column type. 
    df['DELIV_PER'] = df['DELIV_PER'].str.strip()
    df['DELIV_PER'] = df['DELIV_PER'].replace(['-'],'0.00')
    df[['DELIV_PER']] = df[['DELIV_PER']].apply(pd.to_numeric)

    ## DELIV_QTY has some '-' in it. Fix them. Fix the column type. 
    df['DELIV_QTY'] = df['DELIV_QTY'].str.strip()
    df['DELIV_QTY'] = df['DELIV_QTY'].replace(['-'],'0')
    df[['DELIV_QTY']] = df[['DELIV_QTY']].apply(pd.to_numeric)

    ## DELIV_LAC 
    df['DELIV_LACS'] = df.apply (lambda row: (row['AVG_PRICE'] * row['DELIV_QTY'] )//100_000 , axis=1)
    df['DELIV_LACS'] = df['DELIV_LACS'].astype(int)

    ## 
    df['SERIES'] = df['SERIES'].str.strip()

    df = df[df['SERIES']=='EQ']
    df = df.sort_values('DELIV_LACS' , ascending=False)

    ## We would like the date to be in yyyymmdd format. Easier to sort. 
    df['DATE'] = df['DATE1'].apply(convert_date_yyyymmdd)

    return df 

def convert_date_yyyymmdd ( date_string) : 
    parts = date_string.strip().split('-')

    yyyy = parts[2] 
    mm = str(list(calendar.month_abbr).index(parts[1]))
    dd = parts[0]

    return yyyy + mm.zfill(2) + dd