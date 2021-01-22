from PIL import Image


def fixed_size(img, width, height):
    im = Image.open(img)
    out = im.resize((width, height), Image.ANTIALIAS)
    out.save()
