import hello_world 
from reports import get_top_20_deliveries



    # Get the top 20 deliveries for today. 
    # Test 1 - check if we indeed got back 20 rows. 
    # top_20_deliveries = get_top_20_deliveries()
    # assert len(top_20_deliveries) == 20 



    # get_top_20_deliveries('15042021', '13042021')
    # get_top_20_deliveries('15042021')


def test_non_trade_days() : 
    # 14042021 - ambedkar jayanti 
    raw_data_file_full_paths = get_top_20_deliveries('14042021')
    assert len(raw_data_file_full_paths) == 0

    # 14042021 - ambedkar jayanti 
    # '17042021', '18042021' - weekend 
    raw_data_file_full_paths = get_top_20_deliveries('14042021', '17042021', '18042021' )
    assert len(raw_data_file_full_paths) == 0

def test_mix_trade_days() : 
    raw_data_file_full_paths = get_top_20_deliveries('14042021', '15042021', '17042021', '18042021' )
    assert len(raw_data_file_full_paths) == 1


def test_trade_day () : 
    raw_data_file_full_paths = get_top_20_deliveries('15042021')
    assert len(raw_data_file_full_paths) == 1

