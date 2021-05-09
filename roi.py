import logging
import pandas as pd 
import os 
import constants

def fetch_top_minus10_return_amount ( roi_df) : 
    return None

def fetch_return_amount ( roi_df) : 
    return None

def get_file_name (date_string) : 
    
    # logging.debug(f'Fetching data for {date_string}')

    yyyy = date_string[:4]
    mm = date_string[4:6]
    dd = date_string[6:8]

    # logging.debug(f'yyyy {yyyy}, mm {mm}, dd {dd} ')

    prepped_path = '/Users/kaunjovi/code/kuber/data/110_prepped_bhav_copy/sec_bhavdata_full_'

    return prepped_path + dd + mm + yyyy +'.csv'


# Calculate delta on values of consecutive columns. 
def calculate_delta_series ( price_series_df ) : 

    # How to iterate on columns by index ? 
    # We want to start iteration from the second column onwards. 
    # The first column is SYBMOL 
    df_deltas = price_series_df
    data_columns_max = len( price_series_df.columns )
    # logging.debug(f'Number of data columns {data_columns_max}')

    cols_to_drop = []

    # Start from 1. We dont want to touch the column 0 which is SYMBOLS 
    for column in range(1 , data_columns_max) : 
        
        if column < data_columns_max -1 : 

            next_col_name = df_deltas.columns[column + 1 ]
            delta_column = df_deltas.iloc[:, column + 1 ] - df_deltas.iloc[:, column ] 
            df_deltas[next_col_name + '_delta'] = delta_column

        # elif column == data_columns_max : 
            # This is the last data column. There is nothing to compare against 
        
        cols_to_drop.append(column)
                

    df_deltas.drop(df_deltas.columns[cols_to_drop], axis = 1 , inplace=True)

    # add an average column as well. 
    df_deltas['average'] = df_deltas.mean(axis=1)

    df_deltas.to_csv(constants.price_delta_file() , index = False, header=True, quoting=1)
    file_csv = open(constants.price_delta_file(), 'r')
    lines = file_csv.readlines()
    lines.pop(0)


    with open(constants.price_delta_file_js(), 'w') as file_js:
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

    return df_deltas



def generate_price_series ( tickers, date_strings) : 
    # logging.debug(f'Fetching data for {date_strings}')

    dfs = []

    for date_string in date_strings : 
        file_name = get_file_name (date_string)
        if os.path.isfile (file_name ) : 
            date_df = pd.read_csv(file_name)
            date_df = date_df[date_df['SYMBOL'].isin(tickers)] 
            date_df = date_df[date_df['SERIES']== 'EQ'] 
            # date_df = date_df.set_index('SYMBOL', drop=False) 

            column = date_df["DATE1"]
            date_string_from_df = column.max()
            # logging.debug(f'date from data - {date_string_from_df}')

            selected_columns = date_df[["SYMBOL","CLOSE_PRICE"]]
            date_df = selected_columns.copy()
            # date_df.reset_index()

            date_df = date_df.rename( columns = {'CLOSE_PRICE': date_string_from_df } , inplace = False)

            # logging.debug(f'date_df {date_df.head(10)}')

            # if dfs.columns == 0 : 
            #     dfs = date_df
            # else : 

            if isinstance(dfs, list) == True : 
                dfs = date_df
            else :  
                dfs = pd.merge(dfs, date_df, on='SYMBOL')


    return dfs 

if __name__ == "__main__":
    
    logging.basicConfig(format='[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s', level=logging.DEBUG)

    date_strings = ['20200101' , '20200203' , '20200301', '20200401', '20200501', '20200601', '20200701', '20200803', '20200901']
    # tickers = ['RELIANCE', 'HDFC']
    tickers = constants.load_white_list_symbols()
    price_series_df  = generate_price_series ( tickers, date_strings)
    logging.debug(f'\n {price_series_df.head(10)}')

    price_delta_series_df = calculate_delta_series ( price_series_df)
    logging.debug(f'\n {price_delta_series_df.head(10)}')


    # return_amount = fetch_return_amount ( roi_df)
    # top_minus10_return_amount = fetch_top_minus10_return_amount ( roi_df)
     

    