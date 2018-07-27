import base64
import hashlib, uuid, datetime
from common.config import Config

def add_photo(imgstring):
    salt = uuid.uuid4().hex
    hash_image_name = hashlib.sha512(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + salt).hexdigest()

    img_data = b''+ imgstring.split(';')[1].split(',')[1]
    url = hash_image_name + ".png"
    fh = open(Config.static_link + url, "wb")
    fh.write(img_data.decode('base64'))
    fh.close()
    return url

__All__ = []