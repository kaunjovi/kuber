import logging
import pandas as pd 
import src.util as util

# Given a set of trade dates. 
# We assume that bhav data is available 
# In analysis friendly format. 
# And from that data we find the top deliveries 
# For all whitelist tickers
# For all with most amount picked by lakhs 
# For most amount picked by number of shares 
# For most amount picked by % (we might want to filter this)
def fetch_top_deliveries (trade_dates) : 
    
    wl_tickers = whitelist_tickers() 
    delivery_files = [] 

    for trade_date in trade_dates : 
        logging.debug(f'Calculating top deliveries for {trade_date}')

        prepped_file = util.get_prep_file_name(trade_date)
        top_daily_delivery_file_name = util.get_top_daily_delivery_file_name( trade_date)
        logging.debug(f'{top_daily_delivery_file_name}')

        df = pd.read_csv(prepped_file)
        
        # fetch details of only the whitlisted tickers. 
        df_wl = df[ df.SYMBOL.isin(wl_tickers)] 

        # fetch top 1 percentile of those with most deliveries in lakhs 
        df_lakhs = df[ df.DELIV_LACS > df.DELIV_LACS.quantile(.99)]

        # for those with significant delivery numbers i.e > 50 percentile 
        df_lakhs_signi = df[ df.DELIV_LACS > df.DELIV_LACS.quantile(.50)]
        # and those with most number of shares traded. 
        df_traded_qnty = df_lakhs_signi[ df_lakhs_signi.TTL_TRD_QNTY > df_lakhs_signi.TTL_TRD_QNTY.quantile(.99)]
        df_deli_perc = df_lakhs_signi[ df_lakhs_signi.DELIV_PER > df_lakhs_signi.DELIV_PER.quantile(.99)]


        df_big = pd.concat([ df_wl, df_lakhs,df_traded_qnty, df_deli_perc ])
        df_big.sort_values("DELIV_LACS", ascending=False, inplace = True)
        df_big.drop_duplicates(subset ="SYMBOL", inplace = True)

        df_big.to_csv(top_daily_delivery_file_name, index = False, header=True)


    return delivery_files

def whitelist_tickers () : 
    white_list = ['RELIANCE']
    white_list.extend( ['HDFC', 'BAJAJFINSV', 'BAJFINANCE'])
    white_list.extend( [ 'HDFCBANK', 'ICICIBANK', 'KOTAKBANK', 'AXISBANK', 'SBIN', 'IDFCFIRSTB'])
    white_list.extend( [ 'LALPATHLAB' , 'APOLLOHOSP' , 'METROPOLIS' , 'NH'])
    white_list.extend( [ 'RELAXO', 'BATAINDIA'])
    white_list.extend( [ 'DMART', 'TRENT'])
    white_list.extend( [ 'INFY', 'TCS'])
    white_list.extend( [ 'MARUTI', 'M&M', 'MOTHERSUMI'])
    white_list.extend( [ 'ULTRACEMCO', 'JKCEMENT'])

    return white_list 
