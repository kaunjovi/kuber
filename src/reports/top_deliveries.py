import logging
import src.util as util
import pandas as pd 

def generate_top_del_report(trade_dates ) : 

    dfs = []

    for trade_date in trade_dates : 
        top_del_file = util.get_top_daily_delivery_file_name(trade_date) 
        dfs.append(pd.read_csv( top_del_file))

    df_big = pd.concat(dfs, ignore_index=True) 

    df_big.drop('SERIES', axis=1, inplace=True)  
    df_big.drop('DATE1', axis=1, inplace=True)  
    df_big.drop('PREV_CLOSE', axis=1, inplace=True)
    df_big.drop('OPEN_PRICE', axis=1, inplace=True)
    df_big.drop('HIGH_PRICE', axis=1, inplace=True)
    df_big.drop('LOW_PRICE', axis=1, inplace=True)
    df_big.drop('LAST_PRICE', axis=1, inplace=True)
    df_big.drop('TURNOVER_LACS', axis=1, inplace=True)
    df_big.drop('DELIV_QTY', axis=1, inplace=True)
    df_big.drop('NO_OF_TRADES', axis=1, inplace=True)

    logging.debug(f'{df_big.head(10)}')
    
    df_big.to_csv(util.get_top_del_csv_name(), index = False, header=True, quoting=1)

    # Now create the js data array 
    file_csv = open(util.get_top_del_csv_name(), 'r')
    lines = file_csv.readlines()
    lines.pop(0)


    with open(util.get_top_del_js_name(), 'w') as file_js:
        # file_js.write('var dataSet = \n' )
        isTop = True 
        file_js.write('[ \n' )
        for line in lines : 
            if isTop == False : 
                file_js.write(' , \n')
            else : 
                isTop = False
            file_js.write('[' + line + '] ')
        file_js.write(' \n ]')

    return 0
