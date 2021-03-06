# Kuber

- Python. 

# Setup VSCodium to allow push to GitHub

- VSCodium will prompt. 
- If you agree with it, you will get to a closed end. 
- Cancel it. 
- You will get the chance to put in your username and password in VSCodium. 
- That will work. 

# How to setup virtual environment for Python3 development? 

```batch 
kaunjovi@devbook kuber % pipenv run python --version 
Creating a virtualenv for this project...
Pipfile: /Users/kaunjovi/code/kuber/Pipfile
Using /usr/local/bin/python3 (3.9.2) to create virtualenv...
...
... 
Virtualenv location: /Users/kaunjovi/.local/share/virtualenvs/kuber-nxgMKf5O
Creating a Pipfile for this project...
Python 3.9.2
```

## Add unit test dependencies

```
-- unit testing has to be there. 
pipenv install --dev pytest
pipenv install --dev pytest-watch
pipenv install --dev coverage 
```

## And some more dependencies

```
% pipenv install pandas
```

## Run unit test, manually 

```python
## just a mickey mouse unit test 
def test_hello_world() : 
    assert 'Hello world' == 'Hello world'
```

- run manually

```
% pipenv run pytest
``` 

- run automatically everytime any file changes

```
% pipenv run ptw
% pipenv run ptw --ignore ./integration_tests 
```

## HTML report on unit test coverage 

```
/Users/kaunjovi/code/kuber/README.md
% pipenv run coverage run --source=. -m pytest ; pipenv run coverage html
```

## Loggin in Python3

- (Logging in Python)[https://www.datacamp.com/community/tutorials/logging-in-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034358&utm_targetid=aud-522010995285:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9062111&gclid=CjwKCAjw7diEBhB-EiwAskVi1-r_KRXIGk39dWAStUPL7xOmQMnaeIk1aYcJCrtL1ZQ4piNtvrKhDRoCGiYQAvD_BwE]

```python
import logging
...
# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(format='[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s', level=logging.DEBUG)
# logging.basicConfig(format='%(filename)s.%(lineno)s$ %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(filename)s.%(funcName)s().%(lineno)s $$ %(message)s', level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

...
logging.debug(f'Reading data from {len(raw_data_file_full_paths)} files.')



```

## snippet to configure logging 

```json
"Log config": {
    "prefix": "log-config",
    "body": [
        "logging.basicConfig(format='%(funcName)s | %(lineno)d | %(message)s', level=logging.DEBUG)"
    ],
    "description": "Log config"
}
```

```python 

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(format='%(funcName)s | %(lineno)d | %(message)s', level=logging.DEBUG)
# logging.basicConfig(format='[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s', level=logging.DEBUG)
# logging.basicConfig(format='[%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s', level=logging.DEBUG)
logging.basicConfig(format='[%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s', level=logging.DEBUG)

```




https://peaceful-yalow-a1523c.netlify.app/index.html

## data table 

var jsonData = [
    { "meta": { "version": 1, "type": "test" } }
];

$('#table').DataTable({
    "data": jsonData,
    "columns": [
      { "data": "meta.type" },
      { "data": "meta.version" }
    ]
});

$('#example').dataTable( {
    "data": [
        [ "Tiger Nixon", "System Architect", "$3,120", "2011/04/25", "Edinburgh", 5421 ],
        [ "Garrett Winters", "Director", "$8,422", "2011/07/25", "Edinburgh", 8422 ],
        // ...
    ]
} );

$(document).ready(function() {
    $('#example').DataTable();
} );

https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css
https://code.jquery.com/jquery-3.5.1.js
https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js

$(document).ready(function() {
    $('#example').DataTable( {
        data: dataSet,
        columns: [
            { title: "Name" },
            { title: "Position" },
            { title: "Office" },
            { title: "Extn." },
            { title: "Start date" },
            { title: "Salary" }
        ]
    } );
} );

var dataSet = [
    [ "Tiger Nixon", "System Architect", "Edinburgh", "5421", "2011/04/25", "$320,800" ],
]

$.get("logFile", function(response) {
     var logfile = response;
});


# Musings of wannabe financially independent elderly 

Assuming 
    you are alive till ripe old age, 
    and you want to be alive since you are not ailing or grieving, 
    and you have the zeal to actually live a little since you have health, 
you need money. 
Not a heap but an assured tidy little stream. 

You need the money to work for you and make more. 

Stocks is one option if you have time. Please have time. 

You cant time the market. 
Unless you have best mainframes, most number of people, best connection to exchange. 
So, you cant. 

Cant time market. Dont try. 
One and only one truth. LTP. 
Any strategy is not good enough if 
it does not take truth into account
it does not have a safety net. SL. 
it does not give you 20%(?) 
ties me to the desk for hours everyday. 


Get some fu**ing help. Paid help. 
Read some books. 
Take some courses. Data analytics.
Books and courses are not going to cut it. 
You should do that anyway so you know if the cabby is taking the correct road. 

Getting help is important. It is not about ego. It is about kiddo also. 

Learn investing 
- books ? 
- courses ? 

 
Averages over a series of dates 
Delta over a two dates 


https://www.iwillteachyoutoberich.com/blog/make-money-in-stocks/
The quicker you realize that the stock market is not sexy, the faster you will start making money from it.

https://www.iwillteachyoutoberich.com/blog/make-money-in-stocks/

Automate 
    You are not searching for stocks to invest. You have a list and you have a monthly budget. 
    You are not trying to time anything. You just have the month to put the budgeted money in. 


If we take out the to x% (10?) top winning days, what does that do to the earnings. 
What if we ask that about all the shares? Where do we have the most impact ? Any trends on those scrips ? 


Good company, bad results 

Tata consumer products Ltd 

HCl tech 

India mart intermesh 


Intra day trading 
- Do your homework at night. Time it. 
- Action at 1 hr. Time it. 
- 44 SMA. Is it bullish there. 
- Morning. Is this bullish in the morning. First or second candlestick has to be that. 


Chart patterns 
box 
Triangle 
M 
W 
Flag 

Siddharth Bhanushali 

those who missed 
pending orders - in the range 
shorters - they will cover their short 

What is your system ? 

What is double bottom ? 
W. At the bottom we should see big green candle. 


Weekly chart 
Or Daily chart 
Not intraday 

entry - buy at breakout of mid W 
 15 loss shoulg be ok 

Mkt is expensive hobby. None can afford it. 
Bhav bhagwan che

What is back testing ? 

Learn capabilities of charting tools on Kite. 
https://kite.trade/docs/kite/charting/


# Swing Trading For Beginners
https://www.youtube.com/watch?v=vUbvxpUL54c
https://www.youtube.com/watch?v=3AS6qJixHqc
https://www.youtube.com/watch?v=um5SMZg8PiU

Not intraday. 
2 days to months. 

Nifty average movement on a day 
ATR -  A T range 
Reward is unlikely to fit into the range of the day 
Gap up / down is not happening in the day. It happens off the day. Hence not intraday. 

find the direction of the trend first - up or down 
SMA 44 should be the answer


If in swing trading 
    - Dont go in the same stock again 

Stock selection @ weekend 
    44 moving average 
    44 days closing / average 
    Average rising = buy
    Average falling = sell 
    Green candle near moving average 

    Check for entry - at evening 
    Next day - we shall put order. 

    Entry - a little above the top of the candle. 
    SL - lower of the low between candle and candle -1 

    1:2 - SL : TGT 



Daily chart 
    No intraday 
    5 to 10 days 


Bhav bhagwan chhe 

# Risk Management In Stock Market
https://www.youtube.com/watch?v=kB4iz1PggKU

Hedge with option 
Hedge with future 
Allocation in defensive sectors 

# Technical Analysis Of Stocks 
https://www.youtube.com/watch?v=njuFAOEkTMk


## Calculate SMA

- [Moving Averages in pandas](https://www.datacamp.com/community/tutorials/moving-averages-in-pandas)
- [Moving averages with Python](https://towardsdatascience.com/moving-averages-in-python-16170e20f6c)

## Is the trend up or down 


## Detect touch and go in a graph 

- https://stackoverflow.com/questions/59399896/detecting-value-crossing-between-columns-in-pandas















