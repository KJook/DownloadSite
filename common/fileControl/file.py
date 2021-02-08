import os
from .other import *


def create_folder(where, name):
    file_dir = os.sep.join(["static", where])


def reload_file_list_config():
    file_dir = os.sep.join(["static", "src"])  # 以分隔符连接路径名
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        file_list.append([root, files, dirs])

    filename = 'config.txt'
    with open(filename, 'w') as f:
        f.seek(0)
        f.truncate()
        for i in range(len(file_list)):
            f.write(file_list[i][0] + '\n')
            print('*'.join(file_list[i][1]))
            f.write('*'.join(file_list[i][1]) + '\n')
            f.write('*'.join(file_list[i][2]) + '\n')


def get_file(route):
    route = "static" + os.sep + route

    try:
        with open('./config.txt') as f:
            while True:
                line = f.readline()
                if line:
                    if line == route + '\n':
                        return (f.readline().replace('\n', '').split('*'),
                                f.readline().replace('\n', '').split('*')), 200
                    f.readline()
                    f.readline()
                else:
                    return '404 Not Found', 404
    except Exception as e:
        return str(e), 500


def get_size(name, i):
    path = "." + os.sep + "static" + os.sep + name + os.sep + i
    try:
        return size_format(os.path.getsize(path))
    except OSError:
        return "???"
