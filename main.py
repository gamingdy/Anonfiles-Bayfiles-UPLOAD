import requests


class Anonfiles:
    def __init__(self):
        self.based_url = "https://api.anonfiles.com/upload"

    def upload(self, _files):
        print(_files)
        r = requests.post(self.based_url, files=_files)
        print(r.text)
