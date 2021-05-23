import logging 
import trade_engine 

def load_test_case( file_name = 'default_trade_engine_test_case.md') :
    
    if file_name == 'default_trade_engine_test_case.md' : 
        logging.debug(f'Loading defaul test values.')
        sauda = [
                    ['INST', '100' , 'INVST' , 100.00] , 
                    ['INST', '110' , 'B-EQT' , 'GOLD', 100.00 , 1], 
                    ['INST', '120' , 'B-EQT' , 'SLVR', 20.00 , 10]
                ] 
        khata = [
                    ['HSSB', '100' , 100.0, []] ,
                    ['HSSB', '110' , 0.0 , [['GOLD', 100.0 , 1]] ], 
                    ['HSSB', '120' , 0.0 , [['GOLD', 100.0 , 1]] ], 
                ]

        return sauda, khata 

def execute_default() : 
    sauda, khata_expected = load_test_case()
    khata = trade_engine.execute (sauda) 
    return khata_expected == khata

# if __name__ == "__main__":
#     logging.basicConfig(format='%(filename)s.%(funcName)s().%(lineno)s $$ %(message)s', level=logging.DEBUG)
#     logging.debug(f'Hello world from test harness of test engine.')

#     # Load a test case from file. 
#     sauda, khata_expected = load_test_case()
    
#     for instruction in sauda : 
#         logging.debug(f'{ instruction }')
#     for hissab in khata_expected : 
#         logging.debug(f'{hissab}')

#     khata = trade_engine.execute (sauda) 

#     for hissab in khata : 
#         logging.debug(f'{hissab}')

#     if khata_expected == khata : 
#         logging.debug(f'Yaaay')
#     else : 
#         logging.debug(f'Naaaaaayyyy ')
    
