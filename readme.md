# Anonfiles and Bayfiles API wrapper

This is an unoffocial wrapper of Anonfiles/Bayfiles API. It allow you to upload files on Anonfiles or Bayfiles with python.

An exemple of usage 
```py
from Up_file import Anonfiles

anonfiles = Anonfiles()
files_data = anonfiles.upload("path/to/file")  # return a dict with all data like , url/size/files name/files size

# You can also do

from Up_file import Bayfiles

bayfiles = Bayfiles()
files_data = bayfiles.upload("path/to/file")  # return a dict with all data like , url/size/files name/files size
```
