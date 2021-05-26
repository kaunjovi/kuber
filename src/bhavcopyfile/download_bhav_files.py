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
# And, Three - a list of trade dates that were found 
# valid, after this execution. For example a trade date
# might have been passed that did not have bhav file 
# for it online as well. Then that trade date is not valid.  

def download(trade_dates) : 
    bhav_files = [] 
    bhav_files_new = []
    valid_trade_dates = []


    # Loop over the trade dates 
    # Find the file name corresponding to that trade date 
    # If the file exists. All good. Note and move on. 
    # If not. Generate file. Note and move on. 

    for trade_date in trade_dates : 
        bhav_file_to_download = util.get_bhav_file_name(trade_date)

        if os.path.isfile(bhav_file_to_download) == True : 
            logging.debug(f'File already available')
            logging.debug(f'{bhav_file_to_download}')
            bhav_files.append(bhav_file_to_download)
            valid_trade_dates.append(trade_date)
        else : 
            logging.debug(f'Not available {bhav_file_to_download}')
            # TODO : write code to download non existing files. 

    bhav_files.extend(bhav_files_new)

    return valid_trade_dates, bhav_files, bhav_files_new
