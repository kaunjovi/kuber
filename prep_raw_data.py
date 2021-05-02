import logging
import constants
import os 
import util_bhav_file
import pandas as pd 

# Just write the prepped data in the file. 
# Check if the file is there and return yes/no. 
def generate_analysis_ready_bhavdata_overwrite (date_string) : 
    logging.debug(f'Just get the file written.')
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
def prep_sec_bhavdata_full( date_strings) : 
    logging.debug(f'Prepping security bhav data files for detailed analysis.')

    file_count = 0 
    prepped_bhavdata_file_names = []

    # if the file is already there, dont do anything. Just move on. 
    # Action only if the file is not there. 
    for date_string in date_strings : 

        prepped_data_file_full_path = constants.get_full_path_of_prepped_data_file(date_string)
        if os.path.isfile(prepped_data_file_full_path) == False : 
            logging.debug(f'The prepped file {prepped_data_file_full_path} is not available. Creating now.')
            raw_data_file = constants.get_sec_bhavdata_file_name(date_string)
            if os.path.isfile(raw_data_file) : 
                file_created = generate_analysis_ready_bhavdata_overwrite(date_string)
                if file_created == True : 
                    logging.debug(f'{prepped_data_file_full_path} is created now.')
                    file_count += 1 
                    prepped_bhavdata_file_names.append(prepped_data_file_full_path)
                else : 
                    logging.debug(f'{prepped_data_file_full_path} could not be created. Moving on.')
            else : 
                logging.debug(f'Raw data file {raw_data_file} was not present. Moving on.')

        else : 
            logging.debug(f'{prepped_data_file_full_path} already exists.')
            file_count += 1 
            prepped_bhavdata_file_names.append(prepped_data_file_full_path)
        
    return file_count , prepped_bhavdata_file_names


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)
#     date_strings = ['01011919']
#     prep_sec_bhavdata_full(date_strings)

