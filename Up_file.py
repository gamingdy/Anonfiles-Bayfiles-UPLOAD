import requests
import os


class Error(BaseException):
    pass


class Anonfiles:
    def __init__(self):
        self.based_url = "https://api.anonfiles.com/upload"

    def upload(self, filepath):
        with open(filepath, "rb") as a_file:
            filename = os.path.splitext(filepath)[0]
            _files = {"file": (filename, a_file)}
            r = requests.post(self.based_url, files=_files).json()

        if r["status"]:
            file = r["data"]["file"]
            final_file = {
                "url": file["url"],
                "name": file["metadata"]["name"],
                "size": file["metadata"]["size"],
            }

            return final_file
        else:
            r_error = r["error"]
            error_message = f"{r_error['type']} : {r_error['message']}"
            raise Error(error_message)