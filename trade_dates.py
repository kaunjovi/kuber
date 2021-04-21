import logging

def fetch_trade_date_strings (dates_file_name) :
    trade_date_strings = []
    with open(dates_file_name) as f : 
        for line in f : 
            line = line.strip() 
            if len(line) == 0 : 
                logging.debug(f'This is an empty line. Ignore')
            elif line.startswith('#') : 
                logging.debug(f'This is a remark. Ignore.')
            else : 
                trade_date_string = line.partition('#')[0].strip()
                logging.debug(f'{trade_date_string}')
                trade_date_strings.append(trade_date_string)

    return trade_date_strings

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    trade_date_strings = fetch_trade_date_strings('recent.dates')