import logging

# fetch trade dates from recent.dates file. 
# you could make a list in the script, for a few dates. 
# but for larger list, you might want to have a dedicated .dates file. 
def load_file (dates_file_name) :
    trade_date_strings = []
    with open(dates_file_name) as f : 
        for line in f : 
            line = line.strip() 
            if len(line) > 0 and not (line.startswith('#')) : 
                trade_date_string = line.partition('#')[0].strip()
                # logging.debug(f'{trade_date_string}')
                trade_date_strings.append(trade_date_string)

    logging.debug(f'Running process for { len(trade_date_strings)} dates.')
    logging.debug(f'Dates { trade_date_strings}')
    return trade_date_strings

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)
#     trade_date_strings = fetch_trade_date_strings('recent.dates')