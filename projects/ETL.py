import os 
import requests
import pandas as pd
import csv
import sys
from io import StringIO

cwd = os.getcwd()
cwd
path = f"{cwd}\\data\\input\\"

raw_frames = []
for filename in os.listdlr(path):
    f = os.path.join()
