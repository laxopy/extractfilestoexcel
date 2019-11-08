import pandas as pd
import zipfile
import os
from os import listdir
from os.path import isfile, join

zip_dir = input(
    r"Insertar path completo del zip(incluído el nombre del fichero): ")
path, filename = os.path.split(zip_dir)
zip_file = path + '\\' + filename + ".zip"
newfolder = path + '\\' + filename
outputexcel = path + '\\' + filename + ".xlsx"

with zipfile.ZipFile(zip_file) as zip_ref:
    zip_ref.extractall(newfolder)

files_to_insert = [
    f for f in listdir(newfolder)
    if isfile(join(newfolder, f)) and f.endswith('.txt')
]

with pd.ExcelWriter(outputexcel) as writer:
    for filename in files_to_insert:
        gtfsfile = newfolder + '\\' + filename
        df = pd.read_csv(gtfsfile)
        df.to_excel(writer, sheet_name=filename, index=False)
