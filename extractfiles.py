import pandas as pd
from os import listdir
from os.path import isfile, join
from utils.extract_zip import extract_zip
from utils.split_file_name import split_file_name

zip_dir = input('Arrastrar el archivo que quieres exportar '
                'o copia su ruta completa aquí: ')
file_folder, file_name, file_suffix = split_file_name(zip_dir)
output_folder = file_folder / file_name

extract_zip(zip_dir, output_folder)

files_to_insert = [
    f for f in listdir(output_folder)
    if isfile(join(output_folder, f)) and f.endswith('.txt')
]

output_excel = output_folder.with_suffix('.xlsx')
with pd.ExcelWriter(output_excel) as writer:
    for filename in files_to_insert:
        gtfs_file = output_folder / filename
        df = pd.read_csv(gtfs_file)
        df.to_excel(writer, sheet_name=filename, index=False)
