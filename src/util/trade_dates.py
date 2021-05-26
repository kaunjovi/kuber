
# These are the trade dates for which we would like to 
# run the daily reports. Ideally we pick these from a 
# config file. 

def load_trade_dates() : 
    trade_dates = []
    trade_dates.extend(may_2021())
    
    return trade_dates

def may_2021 ( ) : 
    may_2021 = "20210503 20210504 20210505 20210506 20210507 "
# 20210513
    may_2021 += "20210510 20210511 20210512  20210514  "
    may_2021 += "20210517 20210518 20210519 20210520 20210521  "
    may_2021 += "20210524 20210525 20210526   "
    # may_2021 += "20210524 20210525 20210526 20210527 20210528  "
    # may_2021 += "20210531  "

    return list( may_2021.split( ) )

