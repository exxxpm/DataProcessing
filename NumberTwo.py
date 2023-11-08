import shutil
import os
import csv

def create_directory(copy_dir: str) -> str:
    """Создает каталог для копирования датасета."""
    if not os.path.isdir(copy_dir):
        os.mkdir(copy_dir)
    return copy_dir

def copy_dataset(copy_dir: str, annotation_filename: str) -> None:
    """Копирует датасет в другой каталог и создает CSV-файл с параметрами: имя файла и класс файла."""
    create_directory(copy_dir)
    for dataset_item in os.listdir("dataset"):
        files_list = os.listdir(os.path.join("dataset", dataset_item))
        for file_name in files_list:
            shutil.copy(os.path.join(os.path.join("dataset", dataset_item), file_name), os.path.join(copy_dir, f"{dataset_item}_{file_name}"))
        with open(os.path.join(copy_dir, annotation_filename), mode="a", newline='') as file:
            file_writer = csv.writer(file, delimiter=",")
            for file_name in files_list:
                file_writer.writerow([f"{dataset_item}_{file_name}", dataset_item])

def run_copy_dataset(copy_dir: str, annotation_filename: str) -> None:
    copy_dataset(copy_dir, annotation_filename)
