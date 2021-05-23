import logging
import pandas as pd 

def price_movement() : 
    logging.basicConfig(level=logging.DEBUG)

    date_strings = ['01012020', '01022020']
    
    # pick prepped data for a date 
    df = pd.read_csv('/Users/kaunjovi/code/kuber/data/110_prepped_bhav_copy/sec_bhavdata_full_01012020.csv')
    df = df.sort_values("SYMBOL")
    selected_columns = df[["SYMBOL","CLOSE_PRICE"]]
    lean_df = selected_columns.copy()
    lean_df.reset_index(drop = True, inplace=True)
    logging.debug(f'{lean_df.head(10)}')

    # pick prepped data for a date 
    df1 = pd.read_csv('/Users/kaunjovi/code/kuber/data/110_prepped_bhav_copy/sec_bhavdata_full_01022020.csv')
    df1 = df1.sort_values("SYMBOL")
    selected_columns = df1[["SYMBOL","CLOSE_PRICE"]]
    lean_df1 = selected_columns.copy()
    lean_df1.reset_index(drop = True, inplace=True)
    logging.debug(f'{lean_df1.head(10)}')

    # big_df = pd.concat([lean_df, lean_df1], axis=1)
    big_df = pd.merge(lean_df,lean_df1,on='SYMBOL')
    big_df.columns = ['a', 'b', 'c']
    logging.debug(f'{big_df.head(10)}')
    

if __name__ == "__main__":
    price_movement()