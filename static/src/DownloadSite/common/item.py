def return_img_stream(src, name):
    import base64
    img_local_path = getImg(src, name)
    img_stream = ''
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
    return img_stream


def getSuffix(name):
    suffix = name.split(".")
    if len(suffix) == 1 or suffix[0] == '':
        return ''

    return suffix[-1]


def getImg(src, name):
    suffix = getSuffix(name).lower()
    path = ''
    if suffix == 'js':
        path = 'icon/js.png'
    elif suffix == 'css':
        path = 'icon/css.png'
    elif suffix == 'html':
        path = 'icon/html.png'
    elif suffix == 'dart':
        path = 'icon/dart.png'
    elif suffix in ['rar', 'zip', '7z', 'tar', 'gz']:
        path = 'icon/zip.png'
    elif suffix in ['mp3', 'wav']:
        path = 'icon/voice.png'
    elif suffix in ['exe', 'c', 'cpp']:
        path = 'icon/exe.png'
    elif suffix in ['jpg', 'jpeg', 'gif', 'png']:
        path = src + '/' + name
    else:
        path = 'icon/file.png'
    return path, suffix
