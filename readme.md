# Anonfiles and Bayfiles API wrapper

This is an unoffocial wrapper of Anonfiles/Bayfiles API. It allow you to upload files on Anonfiles or Bayfiles with python.

An exemple of usage 
```py
from Up_file import Anonfiles

anonfiles = Anonfiles()
files_data = anonfiles.upload("path/to/file")  


# You can also do

from Up_file import Bayfiles

bayfiles = Bayfiles()
files_data = bayfiles.upload("path/to/file")  # return a dict with all data
```

Exemple:
```py
from Up_file import Anonfiles

anonfiles = Anonfiles()
files_data = anonfiles.upload("test.txt")  


print(files_data)

>>> {'url': {
        'full': 'https://anonfiles.com/h3dc42S6u1/test_txt', 
        'short': 'https://anonfiles.com/h3dc42S6u1'},
        'metadata': {
            'id': 'h3dc42S6u1',
            'name': 'test.txt', 
            'size': {
                'bytes': 6, 
                'readable': '6 B'
                }
            }
        }

```

**NOTE**: *The both return same output*
