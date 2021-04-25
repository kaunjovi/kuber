import configparser

def CONSTANTS():
    if not hasattr(CONSTANTS, 'config_dict'):
        config = configparser.RawConfigParser()
        config.read('kuber.properties')
        CONSTANTS.config_dict = dict(config.items('KUBER'))
        print ("I read the properties file.")
    return CONSTANTS.config_dict

def get_url_to_download_data_from ( date_string) : 
    # return 'https://archives.nseindia.com/products/content/' + 'sec_bhavdata_full_' + date_string + '.csv' 
    return CONSTANTS()['sec_bhavdata_url'] + date_string + '.csv' 

def get_full_path_of_raw_data_file ( date_string) : 
    return CONSTANTS()['sec_bhavdata_folder'] + date_string + '.csv'


# if __name__ == "__main__":
#     print (CONSTANTS()['sec_bhavdata_url'])
