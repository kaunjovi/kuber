import time
from bhav_data import download_sec_bhavdata_full
from bhav_data import generate_analysis_ready_bhavdata

# This is a util file. 
# We are going to use it only to download raw files and prepping that for analysis. 
# This does not need considerations like unit testing etc.
if __name__ == "__main__":
    y = '2020'
    for m in range(1,13) : 
        for d in range (1,32) : 
            date = str(d).zfill(2) + str(m).zfill(2) + str(y) 
            print(f'{date}')
            download_sec_bhavdata_full( [date])
            generate_analysis_ready_bhavdata([date])
            # time.sleep(10)

