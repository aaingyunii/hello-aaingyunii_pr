# hello-aaingyunii_pr `0.3.0`

### INSTALL

`$ pip install hello-aaingyunii_pr`


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

### DEPLOY

`$ pdm publish`
