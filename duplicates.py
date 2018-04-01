import os
import sys
from collections import defaultdict


def get_all_files(directory):
    all_files = defaultdict(list)
    for dirs, subdirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(dirs, file)
            file_size = os.path.getsize(file)
            name_size_together = (file, file_size)
            all_files[name_size_together].append(file_path)
    return all_files


def find_duplicates(all_files):
    duplicate = {}
    for name_size_together, file_path in all_files.items():
        if len(file_path) > 1:
            duplicate.update({name_size_together: file_path})
    return duplicate


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        directory = sys.argv[1]
    else:
        sys.exit('Не задан аргумент или каталог не существует')
    all_files = get_all_files(directory)
    duplicate = find_duplicates(all_files)
    for name_size_together, file_path in duplicate.items():
        print('Файл :', name_size_together[0],
              '\nДублируется :', file_path)
