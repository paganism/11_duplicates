import os
import sys


def get_file_list(directory):
    file_list = []
    for d, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(d, file))
    return file_list


def get_duplicate_list(file_list):
    duplicate_list = []
    for i in range(len(file_list)):
        for j in range(i + 1, len(file_list)):
            if os.path.basename(file_list[i]) == os.path.basename(file_list[j]):
                if os.path.getsize(file_list[i]) == os.path.getsize(file_list[j]):
                    duplicate_list.append(file_list[i])
                    duplicate_list.append(file_list[j])
    return duplicate_list


if __name__ == '__main__':
    directory = sys.argv[1]
    files = get_file_list(directory)
    result_list = get_duplicate_list(files)
    for i in set(result_list):
        print(i)
