from flask import Flask, render_template, url_for, request
from common.fileMaster import getfile, getsize, toSrc_floder
from common.item import getImg
from main import reloadFileConfig
import os

app = Flask(__name__)

@app.route("/u", methods=["POST"])
def getfile():
    where = os.sep.join(request.form["where"].split('/'))
    
    
    file = request.files['file']
    file.save(os.sep.join(["static", request.form["where"],file.filename]))
    reloadFileConfig()
    return {
        "code": "0",
        "msg": "上传成功"
    }

@app.route("/upload")
def uploader():
    where = request.args.get("where")
    return render_template('uoload.html', where=where)

@app.route("/")
def i():
    reloadFileConfig()
    return render_template('index.html')


@app.route("/file/<path:name>")
def index(name):

    f = getfile(name)

    if f[1] == 200 and name[0:3] == 'src':

        fileList = f[0][0]
        folderList = f[0][1]
        data = []

        if len(fileList) > 0:
            for i in fileList:
                if i == '':
                    break
                imgDate = getImg(name, i)
                data.append({
                    "fileName": i,
                    "imgSrc": url_for('static', filename=imgDate[0]),
                    "size": getsize(name, i),
                    "suffix": imgDate[1],
                    "url": name + "/" + i
                })

        folderData = []
        if len(folderList) > 0:
            for i in folderList:
                if i == '':
                    break
                folderData.append({
                    "folderName": i,
                    "toSrc": "/file/" + name + "/" + i
                })

        return render_template('download.html', data=data, folderData=folderData, route="/"+name)
    else:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
