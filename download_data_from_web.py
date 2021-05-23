import logging
import urllib.request
from urllib.error import HTTPError, URLError
from socket import timeout
import shutil
from constants import CONSTANTS
from constants import get_url_to_download_data_from
from constants import get_full_path_of_raw_data_file



# def download_data_for_date_string ( date_string ) : 
#     url_to_download_data_from = get_url_to_download_data_from(date_string)
#     raw_data_file_full_path = get_full_path_of_raw_data_file(date_string)

#     logging.debug(f'Attempting to download data : ')
#     logging.debug(f' for date {date_string}')
#     logging.debug(f' from url {url_to_download_data_from}')
#     logging.debug(f' to file {raw_data_file_full_path}')

#     download_from_url_to_file (url_to_download_data_from, raw_data_file_full_path)

