import logging 

def execute (sauda) : 
    logging.basicConfig(format='%(filename)s.%(funcName)s().%(lineno)s $$ %(message)s', level=logging.DEBUG)
    logging.debug(f'Hello world from test engine.')

    cash = 0.00 
    holdings = []
    khata = []

    for instruction in sauda : 
        # logging.debug(f'{ instruction }')
        instruction_id = instruction[1]

        if instruction[2]== 'INVST' : 
            
            cash += instruction[3]
            holdings_snapshot = list(holdings)
            
            hissab = ['HSSB', instruction_id, cash, holdings_snapshot ]
            # logging.debug(f'{hissab}')
            khata.append(hissab)


        elif instruction[2] =='B-EQT' :
            ticker = instruction[3]
            rate = instruction[4]
            amount = instruction[5]

            if rate * amount <= cash : 
                holding = [ ticker, rate, amount]
                cash = cash - (rate * amount)
                holdings.append(holding)
                holdings_snapshot = list(holdings)

            hissab = ['HSSB', instruction_id, cash, holdings_snapshot ]
            # logging.debug(f'{hissab}')
            khata.append(hissab)

    # logging.debug(f'Cash = {cash}')
    # logging.debug(f'Holdings = {holdings}')

    # logging.debug(f'{khata}')

    return khata
