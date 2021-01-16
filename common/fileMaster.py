import json


def getfile(route):
    try:
        with open('./config.txt') as f:
            while True:
                line = f.readline()
                if line:
                    if line == route + '\n':
                        return f.readline().replace('\n', '').split('*'), 200
                    f.readline()
                else:
                    return '404 Not Found', 404
    except Exception as e:
        return str(e), 500