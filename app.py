from flask import Flask
from common.fileMaster import getfile

app = Flask(__name__)


@app.route("/<path:name>")
def index(name):
    f = getfile(name)
    if f[1] == 200:
        return str(f[0]), 200
    else:
        return f


if __name__ == '__main__':
    app.run(debug=True)
