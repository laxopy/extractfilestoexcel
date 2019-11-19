import zipfile


def extract_zip(zip_dir, output_folder_dir):
    with zipfile.ZipFile(zip_dir) as zip_ref:
        zip_ref.extractall(output_folder_dir)
