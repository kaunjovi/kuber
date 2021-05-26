import logging

def gen_bhav_file_names(trade_dates=['20210526']) :
    file_names = []
    file_name_part1 = '/Users/kaunjovi/code/kuber/data/100_full_bhav_copy/sec_bhavdata_full_'
    file_name_part3 = '.csv'
    for trade_date in trade_dates : 
        yyyy = trade_date[:4]
        mm = trade_date[5:6].zfill(2)
        dd = trade_date[6:8].zfill(2)
        # logging.debug(f'yyyy {yyyy} mm {mm} dd {dd}')
        
        date_bhav_format = dd + mm + yyyy 
        file_name = file_name_part1 + date_bhav_format + file_name_part3
        file_names.append(file_name)

    return file_names

# Given a raw bhav file that we downloaded from the net. 
# We are just looking for the name and location of the 
# file that is prepped for analysis
def gen_prep_file_name ( raw_bhav_file = '') : 
    
    if raw_bhav_file == '' :
        raw_bhav_file = '/Users/kaunjovi/code/kuber/data/100_full_bhav_copy/sec_bhavdata_full_26052021.csv'


    file_name_part1 = '/Users/kaunjovi/code/kuber/data/105_prepped_bhav_copy/'
    file_name_part2 = get_yyyy_mm_dd_from_raw_file_name(raw_bhav_file)
    file_name_part3 = '_sec_bhavdata_full.csv'

    prepped_file_name = file_name_part1 + file_name_part2  + file_name_part3

    return prepped_file_name  
    

# get the date, in the correct format, from the raw data file name. 
def get_yyyy_mm_dd_from_raw_file_name (raw_bhav_file) : 

    yyyy = raw_bhav_file[-8:-4]
    mm = raw_bhav_file[-10:-8].zfill(2)
    dd = raw_bhav_file[-12:-10].zfill(2)
    # logging.debug(f'yyyy {yyyy} mm {mm} dd {dd}')
    
    return yyyy + mm + dd 


    