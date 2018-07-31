import base64
import hashlib, uuid, datetime
import os
from common.config import Config
from django.contrib.staticfiles.templatetags.staticfiles import static


def add_photo(imgstring):
    salt = uuid.uuid4().hex
    path_d = Config.static_link + datetime.datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(path_d):
        os.makedirs(path_d)

    hash_image_name = hashlib.sha512(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + salt).hexdigest()

    img_data = b''+ imgstring.split(';')[1].split(',')[1]
    e_name = imgstring.split(';')[0].split('/')[1]

    url = path_d + '/' + hash_image_name + "." + e_name

    fh = open( url, "wb")
    fh.write(img_data.decode('base64'))
    fh.close()
    return url

__All__ = []