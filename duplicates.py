import os
import sys
from collections import defaultdict


def get_all_file_names(directory):
    all_files = defaultdict(list)
    for dir, subdir, file_name in os.walk(directory):
        for file in file_name:
            file_path = os.path.join(dir, file)
            file_size = os.path.getsize(file)
            name_size_together = (file, file_size)
            all_files[name_size_together].append(file_path)
    return all_files


def find_duplicates(all_files):
    duplicates = {}
    for name_size_tuple, file_path in all_files.items():
        if len(file_path) > 1:
            duplicates.update({name_size_tuple: file_path})
    return duplicates


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        directory = sys.argv[1]
    else:
        sys.exit('Не задан аргумент или каталог не существует')
    all_files = get_all_file_names(directory)
    duplicates = find_duplicates(all_files)
    for name_size_tuple, file_path in duplicates.items():
        print('Файл :', name_size_tuple[0],
              '\nДублируется :', file_path)
