import constants 
import os 
import pandas as pd 
import logging
# from prep_raw_data import prep_sec_bhavdata_full
import trade_dates


def filter_by_white_list (date_strings , white_list = ['KOTAKBANK']) : 
    # row_count = 0  
    dfs = []

    for date_string in date_strings : 
        prepped_data_file = constants.get_full_path_of_prepped_data_file(date_string)
        if os.path.isfile( prepped_data_file) == True : 
            df = pd.read_csv( prepped_data_file)
            df = df[df.SYMBOL.isin(white_list)]
            # df = df.sort_values("DELIV_PER", ascending=False)
            # df = df[df['PREV_CLOSE'] > 100]
            # df = df[df['DELIV_QTY'] > 10_000]

            dfs.append (df)
            # row_count += top 

    big_df = pd.concat(dfs, ignore_index=True)  
    big_df.drop('SERIES', axis=1, inplace=True)  

    big_df.drop('DATE1', axis=1, inplace=True)  
    big_df.drop('PREV_CLOSE', axis=1, inplace=True)  
    big_df.drop('OPEN_PRICE', axis=1, inplace=True)     
    big_df.drop('HIGH_PRICE', axis=1, inplace=True)  
    big_df.drop('LOW_PRICE', axis=1, inplace=True)  
    big_df.drop('LAST_PRICE', axis=1, inplace=True)  

    logging.debug(f' \n {big_df}')

    big_df.to_csv(constants.get_white_list_csv_data_file() , index = False, header=True, quoting=1)

    # Now create the js data array 
    # Using readlines()
    file_csv = open(constants.get_white_list_csv_data_file(), 'r')
    lines = file_csv.readlines()
    lines.pop(0)


    with open(constants.get_white_list_js_data_file(), 'w') as file_js:
        # file_js.write('var dataSet = \n' )
        count_top = 0 
        file_js.write('[ \n' )
        for line in lines : 
            if count_top == 0 : 
                count_top += 1 
            else : 
                file_js.write(' , \n')
            file_js.write('[' + line + '] ')
        file_js.write(' \n ]')



def filter_by_deliv_percentage (date_strings , top= 50) : 
    row_count = 0  
    dfs = []

    for date_string in date_strings : 
        prepped_data_file = constants.get_full_path_of_prepped_data_file(date_string)
        if os.path.isfile( prepped_data_file) == True : 
            df = pd.read_csv( prepped_data_file)
            df = df.sort_values("DELIV_PER", ascending=False)
            df = df[df['PREV_CLOSE'] > 100]
            df = df[df['DELIV_QTY'] > 10_000]

            dfs.append (df.head(top))
            row_count += top 

    big_df = pd.concat(dfs, ignore_index=True)  
    big_df.drop('SERIES', axis=1, inplace=True)  
    big_df.drop('OPEN_PRICE', axis=1, inplace=True)  
    big_df.drop('HIGH_PRICE', axis=1, inplace=True)  
    big_df.drop('LOW_PRICE', axis=1, inplace=True)  
    big_df.drop('LAST_PRICE', axis=1, inplace=True)  

    # logging.debug(f'{big_df}')

    big_df.to_csv(constants.get_top_deliveries_by_percentage_csv_data_file() , index = False, header=True, quoting=1)

    # Now create the js data array 
    # Using readlines()
    file_csv = open(constants.get_top_deliveries_by_percentage_csv_data_file(), 'r')
    lines = file_csv.readlines()
    lines.pop(0)


    with open(constants.get_top_deliveries_by_percentage_js_data_file(), 'w') as file_js:
        # file_js.write('var dataSet = \n' )
        count_top = 0 
        file_js.write('[ \n' )
        for line in lines : 
            if count_top == 0 : 
                count_top += 1 
            else : 
                file_js.write(' , \n')
            file_js.write('[' + line + '] ')
        file_js.write(' \n ]')



def filter_by_deliv_lacs (date_strings , top= 50) : 
    row_count = 0  
    dfs = []

    for date_string in date_strings : 
        prepped_data_file = constants.get_full_path_of_prepped_data_file(date_string)
        if os.path.isfile( prepped_data_file) == True : 
            df = pd.read_csv( prepped_data_file)
            dfs.append (df.head(top))
            row_count += top 

    big_df = pd.concat(dfs, ignore_index=True)  
    big_df.drop('SERIES', axis=1, inplace=True)  
    big_df.drop('OPEN_PRICE', axis=1, inplace=True)  
    big_df.drop('HIGH_PRICE', axis=1, inplace=True)  
    big_df.drop('LOW_PRICE', axis=1, inplace=True)  
    big_df.drop('LAST_PRICE', axis=1, inplace=True)  

    # logging.debug(f'{big_df}')

    big_df.to_csv(constants.get_top_deliveries_by_lacs_csv_data_file(), index = False, header=True, quoting=1)

    # Now create the js data array 
    # Using readlines()
    file_csv = open(constants.get_top_deliveries_by_lacs_csv_data_file(), 'r')
    lines = file_csv.readlines()
    lines.pop(0)


    with open(constants.get_top_deliveries_by_lacs_js_data_file(), 'w') as file_js:
        # file_js.write('var dataSet = \n' )
        count_top = 0 
        file_js.write('[ \n' )
        for line in lines : 
            if count_top == 0 : 
                count_top += 1 
            else : 
                file_js.write(' , \n')
            file_js.write('[' + line + '] ')
        file_js.write(' \n ]')



    return row_count

def filter_by_wl (date_strings , white_list):
    row_count = 0  
    dfs = []

    for date_string in date_strings : 

        # Open data file for the date 
        # If the file exists 
        prepped_data_file = constants.get_full_path_of_prepped_data_file(date_string)
        file_name = constants.get_filtered_by_wl(date_string)
        if os.path.isfile( prepped_data_file) == True : 
            df = pd.read_csv( prepped_data_file)
            
            # filter by white listed symbols.
            df = df[df.SYMBOL.isin(white_list)]
            
            df.to_csv(file_name, index = False, header=True)
            dfs.append(df)
            row_count += len (df.index) 


    big_df = pd.concat(dfs, ignore_index=True)  

    logging.debug(f'{big_df}')

    return row_count

# if __name__ == "__main__":

#     logging.basicConfig(level=logging.DEBUG)

#     white_list = ['RELAXO', 'LALPATHLAB', 'NH']
#     # date_strings = [ '26042021' ,  '27042021' ,  '28042021' ,  '29042021'  ]
#     date_strings = trade_dates.fetch_trade_date_strings('recent.dates')
    
#     prep_sec_bhavdata_full ( date_strings)



#     row_count = filter_by_wl( date_strings, white_list)