import logging
import constants
import os 
import util_bhav_file
import pandas as pd 

# Just write the prepped data in the file. 
# Check if the file is there and return yes/no. 
def generate_analysis_ready_bhavdata_overwrite (date_string) : 
    # logging.debug(f'Just get the file written.')
    df = pd.read_csv(constants.get_full_path_of_raw_data_file(date_string))
    df = util_bhav_file.prep_raw_bhv_data_for_analysis(df)
    # logging.debug(f'{df.head(10)}')
    prepped_file = constants.get_full_path_of_prepped_data_file(date_string)
    df.to_csv(prepped_file, index = False, header=True)
    return os.path.isfile(prepped_file)

# The raw data needs some scrubbing
# The header names need to be stripped. 
# The columns need to have data type explicitly set. 
# All these steps are required for further analyis of this data 
# Do it right at the begining and then you dont have to bother 
# about data quality in further steps 
def for_dates( date_strings) : 

    logging.debug(f'Prepping raw data files [{len(date_strings)}] for detailed analysis.')

    file_count = 0 
    prepped_bhavdata_file_names = []

    for date_string in date_strings : 

        prepped_data_file_full_path = constants.get_full_path_of_prepped_data_file(date_string)
        logging.debug(f'{prepped_data_file_full_path}')

        # if the file is already there, delete it. Create new. 
        if os.path.isfile(prepped_data_file_full_path) == True :
            logging.debug(f'Found the file. Delete old. Try to create new.')
            os.remove(prepped_data_file_full_path)
        else :
            logging.debug(f'File does not exist. Shall try to create new.' ) 

        # Now try to create the prepped file. 
        raw_data_file = constants.get_sec_bhavdata_file_name(date_string)
        if os.path.isfile(raw_data_file) : 
            file_created = generate_analysis_ready_bhavdata_overwrite(date_string)
            if file_created == True : 
                logging.debug(f'File successfully created.')
                file_count += 1 
                prepped_bhavdata_file_names.append(prepped_data_file_full_path)
            else : 
                logging.debug(f'File could not be created. Moving on.')
        else : 

            logging.debug(f'{raw_data_file}')
            logging.debug(f'Raw data file was not present. Moving on.')

        
    return file_count , prepped_bhavdata_file_names


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)

#     date_strings = ['01011919']
#     prep_sec_bhavdata_full(date_strings)

#     date_strings = ['01012020']
#     prep_sec_bhavdata_full(date_strings)

