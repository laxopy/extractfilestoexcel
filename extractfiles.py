import pandas as pd
import zipfile
from os import listdir
from os.path import isfile, join
from pathlib import Path

zip_dir = input(
    r"Arrastrar el archivo que quieres exportar, o copia su ruta completa aquí: ")
file_path = Path(zip_dir)
file_name = file_path.stem
new_folder = file_path.parents[0] / file_name
output_excel = new_folder / file_name
output_excel = output_excel.with_suffix('.xlsx')

with zipfile.ZipFile(file_path) as zip_ref:
    zip_ref.extractall(new_folder)

files_to_insert = [
    f for f in listdir(new_folder)
    if isfile(join(new_folder, f)) and f.endswith('.txt')
]

with pd.ExcelWriter(output_excel) as writer:
    for filename in files_to_insert:
        gtfs_file = new_folder / filename
        df = pd.read_csv(gtfs_file)
        df.to_excel(writer, sheet_name=filename, index=False)
