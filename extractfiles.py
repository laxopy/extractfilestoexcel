import pandas as pd
import zipfile
import os
from os import listdir
from os.path import isfile, join

zip_dir = input(r"Insertar path completo del zip(incluído el nombre del fichero): ")
path, filename = os.path.split(zip_dir)
file = path + '\\' + filename + ".zip"
newfolder = path + '\\' + filename
outputexcel = path + '\\' + filename + ".xlsx"

print(path)
print(file)
print(newfolder)
print(outputexcel)

with zipfile.ZipFile(file) as zip_ref:
    zip_ref.extractall(newfolder)

onlyfiles = [f for f in listdir(newfolder) if isfile(join(newfolder, f))]
print(onlyfiles)

for filename in listdir(newfolder):
    if filename.endswith(".txt"):
        gtfsfile = newfolder+'\\'+filename
        df = pd.read_csv(gtfsfile)
        df.to_excel(outputexcel, sheet_name=filename)
        continue
    else:
        continue

#df = pd.read_csv(newfolder)
#print(df)
#df.to_excel(outputexcel, 'Sheet1')
