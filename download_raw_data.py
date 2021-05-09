import logging
import constants
import os 
import util_bhav_file

def download_sec_bhavdata_full( date_strings) : 
    logging.debug(f'Downloading security bhav data files.')

    file_count = 0 
    sec_bhavdata_full = []

    for date_string in date_strings : 
        raw_data_file_full_path = constants.get_sec_bhavdata_file_name(date_string)

        # if the file is alreday there, job done. 
        # just count, make note and move on. 
        if os.path.isfile(raw_data_file_full_path) == True :
            logging.debug(f'Found {raw_data_file_full_path} locally.')
            file_count += 1 
            sec_bhavdata_full.append(raw_data_file_full_path)
        else :

            # if the file is not available locally
            # try downloading the file. 
            logging.debug(f'Did not find {raw_data_file_full_path} locally.')
            try : 
                url = constants.get_sec_bhavdata_url(date_string)
                util_bhav_file.download_from_url_to_file ( url, raw_data_file_full_path)
                file_count += 1 
                sec_bhavdata_full.append(raw_data_file_full_path)
                logging.debug(f'Downloaded {raw_data_file_full_path} locally.')
            except : 

                # the file could not be downloaded. 
                # might be the url was not available. 
                # dont count this one. The discrepancy would show up. 

                logging.debug(f'Could not download from {url}')

    return file_count , sec_bhavdata_full


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)

#     date_strings = ['01012020']
#     download_sec_bhavdata_full(date_strings)
