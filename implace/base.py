import os
import json
from PIL import Image
from os.path import join as pjoin


IMPLACE_EXTENSIONS = os.environ.get('IMPLACE_EXTENSIONS', ('.png', '.jpg', '.jpeg'))


def create_index(path, idx, append=True):
    if os.path.isfile(idx) and append:
        with open(idx) as fp:
            data = fp.read()
            try:
                data = json.loads(data)
            except Exception:
                data = {}
    else:
        data = {}
    for root, dirs, files in os.walk(path, followlinks=True):
        for fn in files:
            base, ext = os.path.splitext(fn)
            full_path = pjoin(root, fn)
            name = full_path.replace(path, '', 1).strip('/')
            if name not in data and ext in IMPLACE_EXTENSIONS:
                im = Image.open(full_path)
                data[name] = list(im.size)
    with open(idx, 'w') as fp:
        fp.write(json.dumps(data))


def create_images(path, idx):
    if os.path.isfile(idx):
        with open(idx) as fp:
            data = fp.read()
            try:
                data = json.loads(data)
            except Exception:
                return
    else:
        return
    for name, size in data.iteritems():
        full_path = pjoin(path, name)
        if not os.path.isfile(full_path):
            Image.new('L', size).save(pjoin(path, name))

