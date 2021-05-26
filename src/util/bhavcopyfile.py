import logging

# Find corresponding bhav file name, given a trade date. 
def get_bhav_file_name(trade_date='20210526') :
    file_name_part1 = '/Users/kaunjovi/code/kuber/data/100_full_bhav_copy/sec_bhavdata_full_'

    ddmmyyyy = get_ddmmyyyy ( trade_date)
        
    file_name_part3 = '.csv'

    return file_name_part1 + ddmmyyyy + file_name_part3

# We are just looking for the name and location of the 
# file that is prepped for analysis
def get_prep_file_name ( trade_date='20210526') : 
    
    file_name_part1 = '/Users/kaunjovi/code/kuber/data/105_prepped_bhav_copy/'
    file_name_part2 = trade_date
    file_name_part3 = '_sec_bhavdata_full.csv'

    prepped_file_name = file_name_part1 + file_name_part2  + file_name_part3

    return prepped_file_name  

def get_top_daily_delivery_file_name ( trade_date='20210526') : 
    part1 = '/Users/kaunjovi/code/kuber/data/220_top_daily_deliveries/'
    part2 = trade_date
    part3 = '_top_daily_delivery.csv'

    return part1 + part2 + part3
    

def get_ddmmyyyy (trade_date) : 
    yyyy = trade_date[:4]
    mm = trade_date[5:6].zfill(2)
    dd = trade_date[6:8].zfill(2)
    return dd + mm + yyyy

# get the date, in the correct format, from the raw data file name. 
def get_yyyy_mm_dd_from_raw_file_name (raw_bhav_file) : 

    yyyy = raw_bhav_file[-8:-4]
    mm = raw_bhav_file[-10:-8].zfill(2)
    dd = raw_bhav_file[-12:-10].zfill(2)
    # logging.debug(f'yyyy {yyyy} mm {mm} dd {dd}')
    
    return yyyy + mm + dd 


    