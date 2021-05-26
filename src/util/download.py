import urllib.request
from urllib.error import HTTPError, URLError
from socket import timeout
import shutil


# Download text from url and save it in a local file. 
# Raise error if you cant. Most likely becuase the url was not existent. 
# Can be moved to util actually
def download_url_to_file(url, file) : 
    try:
        with urllib.request.urlopen(url, timeout=10) as response, open(file, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except timeout:
        # logging.exception(f'Could not download data from {url_to_download_data_from}')
        raise
