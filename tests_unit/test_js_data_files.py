import js_data_files
import os 
import constants

def test_generate_top_daily_deliveries_js( ) : 

    tag_test = 'test'

    # Clean up files if they were already there. 
    # These are files tagged 'test'. So safe to delete. 
    if os.path.exists( constants.get_top_deliveries_js_data_file(tag_test)) : 
        os.remove( constants.get_top_deliveries_js_data_file(tag_test))

    if os.path.exists( constants.get_top_deliveries_csv_data_file(tag_test) ) : 
        os.remove( constants.get_top_deliveries_csv_data_file(tag_test))

    # Now call the method under test. 
    date_strings = ['05042021']
    js_data_files.generate_top_daily_deliveries_js(date_strings , tag_test)

    # if the files were created, at least shallow check has passed. 
    if os.path.exists( constants.get_top_deliveries_js_data_file(tag_test)) : 
        os.remove( constants.get_top_deliveries_js_data_file(tag_test))
        assert True
    else : 
        assert False

    if os.path.exists( constants.get_top_deliveries_csv_data_file(tag_test) ) : 
        os.remove( constants.get_top_deliveries_csv_data_file(tag_test))
        assert True
    else : 
        assert False
