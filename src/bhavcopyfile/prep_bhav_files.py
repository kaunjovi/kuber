import src.util as util
import logging
import pandas as pd 
import os 
import calendar

# The raw files are great for data. We want to have a copy as it is. 
# However, before you do any analysis you want to make some changes. 
# For example, you definitely want to change the date to YYYYMMDD format. 
# Also, you want the delivery picked in lakhs.
# And other changes. 
# These result in modified files and hence have to be kept 
# separate from the raw

def prep_for_analysis (raw_bhav_files) : 
    prepped_bhav_files = []
    prepped_bhav_files_new = []

    for raw_bhav_file in raw_bhav_files : 
        prep_file_name = util.gen_prep_file_name( raw_bhav_file)
        if os.path.isfile(prep_file_name) : 
            logging.debug(f'Prepped file exists already.')
            logging.debug(f'{prep_file_name}')
            prepped_bhav_files.append(prep_file_name)
        else : 
            logging.debug(f'Prepped file does not exist.')
            logging.debug(f'{prep_file_name}')
            isFileCreated = generate_prepped_bhav_copy( raw_bhav_file, prep_file_name)
            if isFileCreated == True : 
                prepped_bhav_files_new.append(prep_file_name)

    prepped_bhav_files.extend( prepped_bhav_files_new)
            
    return prepped_bhav_files, prepped_bhav_files_new

# Generate the prepped file without any checks.
# If the file exists, just overwrite it. 
def generate_prepped_bhav_copy ( raw_file, prepped_file ) : 
    logging.debug(f'Raw file {raw_file}')
    logging.debug(f'Prepped file {prepped_file}')

    df = pd.read_csv(raw_file)

    # Get rid of whitespaces in the headers
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

    df.to_csv(prepped_file, index = False, header=True)

    return os.path.isfile(prepped_file)

# We need to convert 25-May-2021 to 20210525, format wise 
def convert_date_yyyymmdd ( date_string) : 
    parts = date_string.strip().split('-')

    yyyy = parts[2] 
    mm = str(list(calendar.month_abbr).index(parts[1]))
    dd = parts[0]

    return yyyy + mm.zfill(2) + dd
