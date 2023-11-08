import random
import os
import shutil
import csv
from typing import Optional
from NumberTwo import create_directory

def get_file_names(class_name: str) -> Optional[str]:
    """Возвращает список имен файлов в классе датасета."""
    for file_name in os.listdir(os.path.join("dataset", class_name)):
        yield file_name

def create_random_file_names(annotation_filename: str, copy_dir: str) -> None:
    """Создает копии датасета в другом каталоге с произвольными именами файлов."""
    file_numbers = list(range(10001))
    random.shuffle(file_numbers)
    counter = 1
    create_directory(copy_dir)
    for dataset_class in os.listdir("dataset"):
        for file_name in get_file_names(dataset_class):
            shutil.copy(os.path.join(os.path.join("dataset", dataset_class), file_name), os.path.join(copy_dir, f"{file_numbers[counter]}.txt"))
            with open(os.path.join(copy_dir, annotation_filename), mode="a", newline='') as file:
                file_writer = csv.writer(file, delimiter=",")
                file_writer.writerow([f"{file_numbers[counter]}.txt", dataset_class])
            counter += 1

def run_random_file_names(annotation_filename: str, copy_dir: str) -> None:
    create_random_file_names(annotation_filename, copy_dir)
