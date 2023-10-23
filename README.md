# hello-aaingyunii_pr `1.0.0`

- The Python program I'm distributing for the first time

View at:

- https://pypi.org/project/hello-aaingyunii_pr

### INSTALL
`$ pip install hello-aaingyunii_pr`

### USE

```bash
$ hello-aaingyunii-pic



            ░░░░░░░░░░░░░░░░░░░░░░░░░░
            ░░░█▀▀▀░█▀▀█░░█▀▀░▀▀█░░█░░
            ░░░▀▀▀█░█░░█░░█▀▀░▄▀░░░▀░░
            ░░░▀▀▀▀░▀▀▀▀░░▀▀▀░▀▀▀░░▀░░
            ░░░░░░░░░░░░░░░░░░░░░░░░░░
            ⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞⎛⎝(•‿•)⎠⎞

```

```bash
$ hello-aaingyunii-who

My name is aik

```


```bash
$ ha-weather

현재 날씨: 맑음
현재 온도: 16.9°

```

### DEV

```bash
$ git clone ...
$ cd hello-aaingyunii_pr
$ pdm venv create
$ source .venv/bin/activate
(hello-aaingyunii_pr-3.8) $ pdm install
```

### TEST

```bash
$ pdm add -dG test pytest pytest-cov
$ pytest
$ pytest -s
$ pytest --cov
```

### `pytest` 

- who.py
```python
def my_name():
    print("My name is aik")
```

- test_who.py
```python
from hello_aaingyunii_pr.who import my_name

def test_my_name():
    my_name()
```

- test_weather.py 
```python
from hello_aaingyunii_pr.weather_show import weather_show

def test_weather():
    weather_show()
    assert True
```

### DEPLOY

```bash
$ pdm publish
```

### REF
- image to text : https://www.text-image.com/convert/ascii.html
- weather data : https://weather.naver.com/




