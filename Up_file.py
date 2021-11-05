import requests
import os


class Error(BaseException):
    pass


class UploadFile:
    def __init__(self, url, get_url):
        self.based_url = url
        self.file_url = get_url

    def _data(self, request_result):

        if request_result["status"]:

            file = request_result["data"]["file"]
            final_file = {"url": file["url"], "metadata": file["metadata"]}

            return final_file

        else:

            r_error = request_result["error"]
            error_message = f"{r_error['type']} : {r_error['message']}"

            raise Error(error_message)

    def upload(self, filepath):
        """
        Upload files on Anonfiles or Bayfiles, with a Size limit to 5 Go/Gb by files.
        You must be specified files path(relative or absolute)
        """

        with open(filepath, "rb") as a_file:
            filename = os.path.basename(filepath)
            _files = {"file": (filename, a_file)}
            r = requests.post(self.based_url, files=_files).json()

        return _data(r)

    def get_file(self, file_id):
        r = requests.get(f"{self.file_url}/{file_id}/info").json()

        if r["status"]:
            file = r["data"]["file"]
            final_file = {"url": file["url"], "metadata": file["metadata"]}

            return final_file
        else:
            r_error = r["error"]
            error_message = f"{r_error['type']} : {r_error['message']}"
            raise Error(error_message)


class Anonfiles(UploadFile):
    """
    This class allow you upload files to Anonfiles using the Anonfiles API
    """

    def __init__(self):
        base_url = "https://api.anonfiles.com/upload"
        get_file_url = "https://api.anonfiles.com/v2/file"
        UploadFile.__init__(self, base_url, get_file_url)


class Bayfiles(UploadFile):
    """
    This class allow you upload files to Bayfiles using the Bayfiles API
    """

    def __init__(self):
        base_url = "https://api.bayfiles.com/upload"
        get_file_url = "https://api.bayfiles.com/v2/file"
        UploadFile.__init__(self, base_url, get_file_url)
