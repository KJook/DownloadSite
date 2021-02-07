import os

def reloadFileConfig():
    fileDir = os.sep.join(["static", "src"])  # 以分隔符连接路径名
    fileList = []
    for root, dirs, files in os.walk(fileDir):
        fileList.append([root, files, dirs])

    filename = 'config.txt'
    with open(filename, 'w') as f:
        f.seek(0)
        f.truncate()
        for i in range(len(fileList)):
            f.write(fileList[i][0] + '\n')
            print('*'.join(fileList[i][1]))
            f.write('*'.join(fileList[i][1]) + '\n')
            f.write('*'.join(fileList[i][2]) + '\n')
