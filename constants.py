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


def get_data_folder() : 
    return '/Users/kaunjovi/code/kuber/data/'

def get_sec_bhavdata_file_name (date_string) : 
    return get_data_folder() + '100_full_bhav_copy/sec_bhavdata_full_'+date_string+'.csv'

def get_sec_bhavdata_url (date_string) : 
    return 'https://archives.nseindia.com/products/content/sec_bhavdata_full_' + date_string + '.csv' 
    
def get_top_delivery_file_name(date_string) : 
    return get_data_folder() + '200_top_daily_deliveries/top_deliveries_'+date_string+'.csv'

def get_top_average_delivery_file_name () : 
    return get_data_folder() + '300_top_daily_average/top_average_deliveries.csv'

def get_top_deliveries_file_quoted_first_step() : 
    return get_data_folder() + '400_js_data/top_deliveries_quoted_1.csv'

def get_top_deliveries_js_data_file() : 
    return '/Users/kaunjovi/code/kuber-online/data.js' 

# if __name__ == "__main__":
#     print (CONSTANTS()['sec_bhavdata_url'])
