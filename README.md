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
% pipenv run coverage run --source=. -m pytest ; pipenv run coverage html
```

## Loggin in Python3

```python
import logging
...
logging.basicConfig(level=logging.DEBUG)
...
logging.debug(f'Reading data from {len(raw_data_file_full_paths)} files.')
```
