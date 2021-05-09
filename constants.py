import configparser
import logging

def CONSTANTS():
    logging.basicConfig(level=logging.DEBUG)
    if not hasattr(CONSTANTS, 'config_dict'):
        config = configparser.RawConfigParser()
        config.read('kuber.properties')
        CONSTANTS.config_dict = dict(config.items('KUBER'))
        # print ("I read the properties file.")
        logging.debug(f'Properties file was loaded in memory.')
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





def get_top_deliveries_by_percentage_csv_data_file( tag='default') :
    if tag== 'default' :  
        return get_data_folder() + '400_js_data/top_deliveries_by_percentage.csv'
    else : 
        return get_data_folder() + '400_js_data/top_deliveries_by_percentage_' + tag + '.csv' 

def get_top_deliveries_by_percentage_js_data_file( tag='default') :
    if tag== 'default' :  
        return get_data_folder() + '400_js_data/top_deliveries_by_percentage.js'
    else : 
        return get_data_folder() + '400_js_data/top_deliveries_by_percentage_' + tag + '.js' 

def get_top_deliveries_by_lacs_csv_data_file( tag='default') :
    if tag== 'default' :  
        return get_data_folder() + '400_js_data/top_deliveries_by_lacs.csv'
    else : 
        return get_data_folder() + '400_js_data/top_deliveries_by_lacs_' + tag + '.csv' 

def get_top_deliveries_by_lacs_js_data_file( tag='default') :
    if tag== 'default' :  
        return get_data_folder() + '400_js_data/top_deliveries_by_lacs.js'
    else : 
        return get_data_folder() + '400_js_data/top_deliveries_by_lacs_' + tag + '.js' 

def get_top_deliveries_js_data_file(tag='default') :
    if tag== 'default' :  
        return '/Users/kaunjovi/code/kuber/data/400_js_data/top_deliveries.js' 
    else : 
        return '/Users/kaunjovi/code/kuber/data/400_js_data/top_deliveries_' + tag + '.js' 


def get_full_path_of_prepped_data_file ( date_string ) : 
    path = get_data_folder() + '110_prepped_bhav_copy/sec_bhavdata_full_'
    path += date_string
    path += '.csv'
    return path  

def get_filtered_by_wl(date_string) : 
    path = get_data_folder() + '210_filtered_by_wl/filtered_by_wl_'
    path += date_string
    path += '.csv'
    return path  


# symbols that we want to look into anyway
# might be by doing fundamental analysis offline. 
# you want to pick this from a file
def load_white_list_symbols(): 
    white_list = ['RELIANCE', 'HDFC', 'BAJAJFINSV', 'BAJFINANCE']
    white_list.extend( [ 'HDFCBANK', 'ICICIBANK', 'KOTAKBANK', 'AXISBANK', 'SBIN', 'IDFCFIRSTB'])
    white_list.extend( [ 'LALPATHLAB' , 'APOLLOHOSP' , 'METROPOLIS' , 'NH'])
    white_list.extend( [ 'RELAXO', 'BATAINDIA'])
    white_list.extend( [ 'DMART', 'TRENT'])
    white_list.extend( [ 'INFY', 'TCS'])
    white_list.extend( [ 'MARUTI', 'M&M', 'MOTHERSUMI'])
    white_list.extend( [ 'JKCEMENT'])


    return white_list 


def get_white_list_csv_data_file(tag='default') :
    if tag== 'default' :  
        return '/Users/kaunjovi/code/kuber/data/400_js_data/top_wl_deliveries.csv' 
    else : 
        return '/Users/kaunjovi/code/kuber/data/400_js_data/top_wl_deliveries_' + tag + '.csv' 

def get_white_list_js_data_file(tag='default') :
    if tag== 'default' :  
        return '/Users/kaunjovi/code/kuber/data/400_js_data/top_wl_deliveries.js' 
    else : 
        return '/Users/kaunjovi/code/kuber/data/400_js_data/top_wl_deliveries_' + tag + '.js' 

def price_delta_file(tag='default') :
    if tag== 'default' :  
        return '/Users/kaunjovi/code/kuber/data/400_js_data/price_delta_series.csv' 
    else : 
        return '/Users/kaunjovi/code/kuber/data/400_js_data/price_delta_series_' + tag + '.csv' 

def price_delta_file_js(tag='default') :
    if tag== 'default' :  
        return '/Users/kaunjovi/code/kuber/data/400_js_data/price_delta_series.js' 
    else : 
        return '/Users/kaunjovi/code/kuber/data/400_js_data/price_delta_series_' + tag + '.js' 



# if __name__ == "__main__":
#     print (CONSTANTS()['sec_bhavdata_url'])

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)
#     logging.debug(f'Checking constants file.')
#     for symbol in get_whitelist() : 
#         logging.debug(f'{symbol}')


