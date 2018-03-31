import os
import sys


def get_file_list(directory):
    file_list = []
    for d, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(d, file))
    return file_list


def get_duplicates(file_list):
    duplicates = {}
    files_parameters = {}
    for file in file_list:
        if (os.path.basename(file),
                os.path.getsize(file)) in files_parameters.keys():
            try:
                duplicates[os.path.basename(file)].append(file)
            except KeyError:
                duplicates[os.path.basename(file)] = [
                    file,
                    files_parameters.get((
                        os.path.basename(file),
                        os.path.getsize(file))
                    )]
        else:
            files_parameters[
                os.path.basename(file),
                os.path.getsize(file)] = file
    return duplicates


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        directory = sys.argv[1]
    else:
        sys.exit('Не задан аргумент или каталог не существует')
    file_list = get_file_list(directory)
    dups = get_duplicates(file_list)
    for file, path in dups.items():
        print(file, path)
