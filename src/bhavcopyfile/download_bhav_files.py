import logging
import os 
import src.util as util

# Download the bhav copy files from website. 
# Given the trade dates, check if the file is already 
# available locally. If yes, dont download. Just report. 
# If the file is not already available, then download.
# Two list of files have to be reproted. 
# One - list of all files available locally at the end 
# of execution. 
# Two - list of all files that were downloaded fresh
# during this execution. 

def download(trade_dates) : 
    bhav_files = [] 
    fresh_bhav_files = []

    # Get the names and location of the local files that we
    # need for each trade date. 
    logging.debug(f'Converting {len(trade_dates)} trade dates to their corresponding file names.')
    bhav_files_to_download = util.gen_bhav_file_names(trade_dates)

    # Check for the files that are confirmed available. 
    bhav_files_available = []
    for bhav_file_to_download in bhav_files_to_download : 
        if os.path.isfile(bhav_file_to_download) == True : 
            logging.debug(f'File already available')
            logging.debug(f'{bhav_file_to_download}')
            bhav_files_available.append(bhav_file_to_download)
        else : 
            logging.debug(f'Not available {bhav_file_to_download}')
            # TODO : write code to download non existing files. 
    
    bhav_files.extend(bhav_files_available)
    bhav_files.extend(fresh_bhav_files)

    return bhav_files, fresh_bhav_files