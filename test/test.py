import sys
import os

sys.path.insert(0, os.path.abspath(".."))

from pyUpload import Bayfiles


fi = Bayfiles().upload("test.txt")

print(fi)
