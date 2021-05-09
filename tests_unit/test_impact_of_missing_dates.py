# Test the impact of missing dates on mkt. 
# The theory being if you are out of mkt for a handful 
# of dates you could miss most of the benefit. 
# Hence the argument being that you should stay put in the mkt. 
# However, 
# this also means that you are not to get out of mkt 
# when you feel things are gonig bad. As in you are not to 
# have SL. Or at least not agressive SL. 

import roi 

def test_impact_of_missing_dates( ) :

    # Lets start small. Single SYMBOL. Only two dates. 
    price_series_df  = roi.generate_price_series ( ['RELIANCE'], ['20200101' , '20200102' ])
    assert len(price_series_df) == 1 
    assert len( price_series_df.columns ) == 3 

    # For two columns, the difference column, shall be only one. 
    # However, there is an average column as well. So the count becomes same. 
    price_delta_series = roi.calculate_delta_series(price_series_df )
    assert len(price_delta_series) == 1 
    assert len( price_delta_series.columns ) == 3


