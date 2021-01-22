import os


def toSrc_floder(name, i):
    return name + os.sep + i


def getfile(route):
    route = "static" + os.sep + route

    try:
        with open('./config.txt') as f:
            while True:
                line = f.readline()
                if line:
                    if line == route + '\n':
                        return (f.readline().replace('\n', '').split('*'), f.readline().replace('\n', '').split('*')), 200
                    f.readline()
                    f.readline()
                else:
                    return '404 Not Found', 404
    except Exception as e:
        return str(e), 500


def getsize(name, i):
    path = "." + os.sep + "static" + os.sep + name + os.sep + i
    try:
        return size_format(os.path.getsize(path))
    except:
        return "???"


def size_format(size):
    if size < 1000:
        return '%i' % size + 'size'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size/1000) + 'KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size/1000000) + 'MB'
    elif 1000000000 <= size < 1000000000000:
        return '%.1f' % float(size/1000000000) + 'GB'
    elif 1000000000000 <= size:
        return '%.1f' % float(size/1000000000000) + 'TB'