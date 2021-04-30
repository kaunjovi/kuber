# import os
# import logging
import pandas as pd 
# from  constants import get_top_delivery_file_name
# from  constants import get_sec_bhavdata_file_name


def prep_raw_bhv_data_for_analysis ( df ) : 
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

    return df 