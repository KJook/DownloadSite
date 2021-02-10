import os

from flask import Flask, render_template, url_for, request, jsonify, make_response

import common.fileControl as FileController
import common.itemControl as ItemController

import base64
import urllib.parse

app = Flask(__name__)


@app.route("/d", methods=["POST"])
def delet():
    raw_full_path = request.form["w"]
    file_list = request.form["fi"].split('*')
    folder_list = request.form["fo"].split('*')

    full_path = urllib.parse.unquote(base64.b64decode(raw_full_path).decode("utf-8"))
    try:
        if not file_list[0] == '':
            for file in file_list:
                FileController.move_to_trash(full_path, file)
        if not folder_list[0] == '':
            for folder in folder_list:
                FileController.move_to_trash(full_path, folder)
    except OSError as e:
        return make_response(jsonify({"code": "0", "error": str(e)}), 500)
    else:
        return make_response(jsonify({"code": "0", "error": "null"}), 200)



@app.route("/createFolder", methods=["POST"])
def create_folder():
    where = request.form["where"]
    name = request.form["name"]
    file_handle = FileController.create_folder(where, name)
    if file_handle[1] == 200:
        return make_response(jsonify({"code": "0", "error": "null"}), 200)
    else:
        return make_response({"code": 1, "error": file_handle[0]}, 500)


@app.route("/u", methods=["POST"])
def getfile():
    file = request.files['file']
    file.save(os.sep.join(["static", request.form["where"], file.filename]))
    FileController.reload_file_list_config()
    return {
        "code": "0",
        "msg": "上传成功"
    }


@app.route("/upload")
def uploader():
    where = request.args.get("where")
    return render_template('upload.html', where=where)


@app.route("/")
def i():
    FileController.reload_file_list_config()
    return render_template('index.html')


@app.route("/file/<path:name>")
def index(name):
    f = FileController.get_file(name)
    if f[1] == 200 and name[0:3] == 'src':

        file_list = f[0][0]
        folder_list = f[0][1]
        data = []

        if len(file_list) > 0:
            for file in file_list:
                if file == '':
                    break
                img_date = ItemController.get_img(name, file)
                data.append({
                    "fileName": file,
                    "imgSrc": url_for('static', filename=img_date[0]),
                    "size": FileController.get_size(name, file),
                    "suffix": img_date[1],
                    "url": name + "/" + file
                })

        folder_data = []
        if len(folder_list) > 0:
            for folder in folder_list:
                if folder == '':
                    break
                folder_data.append({
                    "folderName": folder,
                    "toSrc": "/file/" + name + "/" + folder
                })

        return render_template('download.html', data=data, folderData=folder_data, route="/" + name)
    else:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
