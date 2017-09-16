#!/usr/bin/env python
import urllib.request
import os
import os.path as osp
import hashlib


def download_images():
    url = 'http://zhjwxk.cic.tsinghua.edu.cn/login-jcaptcah.jpg?captchaflag=login1'
    if not osp.exists('images300'):
        os.makedirs('images300')
    images_hash = set()
    image_count = 0
    while True:
        r = urllib.request.get(url)
        image_fname = osp.join('images300', '%06d.jpg' % image_count)
        image_hash = hashlib.md5()
        image_hash.update(r.content)
        image_hash = image_hash.hexdigest()
        if image_hash not in images_hash:
            with open(image_fname, 'wb') as f:
                f.write(r.content)
            images_hash.add(image_hash)
            image_count += 1
        if image_count == 300:
            break


def main():
    download_images()


if __name__ == '__main__':
    main()
