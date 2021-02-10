import os
import time
import shutil
from .other import *


def move_to_trash(full_path, f):
    f_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    shutil.move(os.sep.join(['static', full_path, f]),  os.sep.join(['static', 'trash']))
    os.rename(os.sep.join(['static', 'trash', f]), os.sep.join(['static', 'trash', f_time + f]))
    reload_file_list_config()


def create_folder(where, name):
    if '/' in name or '*' in name or '\\' in name:
        return "folder name is invalid", 500
    if (not where[0:4] == '/src') or ('.' in where):
        return "a big problem is caused. maybe some guy is trying to attack this website.", 500

    file_dir = os.sep.join(["static", url_path(where), name])
    try:
        os.mkdir(file_dir, 0o755)
        reload_file_list_config()
    except OSError as e:
        return str(e), 500
    else:
        return "ok", 200


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
