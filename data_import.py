import pyedflib
import pandas
import os
from pathlib import Path, PosixPath


path = "/Users/markmorley/Desktop/DATALOG/20221201"
dir_list = os.listdir(path)
edfs = []

for file in dir_list:
    if file[-3:] == "edf":
        edfs.append(file)

filepath = f"{path}/20221201_235234_PLD.edf"

f = pyedflib.EdfReader(filepath)
birth = f.getHeader()
print(f.getSampleFrequency(0))
