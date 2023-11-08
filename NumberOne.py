import os
import csv

def create_csv_annotation(class_name: str, annotation_filename: str) -> None:
    """Генерирует CSV-аннотацию на основе класса и имени файла."""
    dataset_path = os.path.join('dataset')
    class_names = os.listdir(dataset_path)
    with open(annotation_filename, mode="w", newline='') as file:
        file_writer = csv.writer(file, delimiter=",")
        for name in class_names:
            file_writer.writerow([os.path.abspath(name), os.path.join(dataset_path, name), class_name])

def run_annotation_generation(class_name: str, annotation_filename: str) -> None:
    create_csv_annotation(class_name, annotation_filename)
