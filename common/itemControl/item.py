def get_suffix(name):
    suffix = name.split(".")
    if len(suffix) == 1 or suffix[0] == '':
        return ''
    return suffix[-1]


def get_img(src, name):
    suffix = get_suffix(name).lower()
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
