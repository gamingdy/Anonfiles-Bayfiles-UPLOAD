import requests
import os


class Error(BaseException):
    pass


class UploadFile:
    def __init__(self, url):
        self.based_url = url

    def upload(self, filepath):
        with open(filepath, "rb") as a_file:
            filename = os.path.basename(filepath)
            _files = {"file": (filename, a_file)}
            r = requests.post(self.based_url, files=_files).json()

        if r["status"]:
            file = r["data"]["file"]
            final_file = {"url": file["url"], "metadata": file["metadata"]}

            return final_file
        else:
            r_error = r["error"]
            error_message = f"{r_error['type']} : {r_error['message']}"
            raise Error(error_message)


class Anonfiles(UploadFile):
    def __init__(self):
        UploadFile.__init__(self, "https://api.anonfiles.com/upload")


class Bayfiles(UploadFile):
    def __init__(self):
        UploadFile.__init__(self, "https://api.bayfiles.com/upload")
