#!/usr/bin/env python
import cv2
import pickle
import numpy as np


def predict(image, model):
    hog = cv2.HOGDescriptor()
    feature = hog.compute(cv2.resize(image, (64, 128)))[:, 0]
    diff = feature - model['feature']
    diff = np.linalg.norm(diff, axis=1)
    label = model['label'][diff.argmin()]
    return label


def demo300():
    from glob import glob
    import matplotlib.pyplot as plt
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    images_fname = glob('./images300/*.jpg')
    for image_fname in images_fname:
        gt_label = image_fname.split('/')[-1].split('.')[0]
        image = cv2.imread(image_fname)
        # Test procedure
        # 1. Read image into numpy array
        # 2. invoke predict() function
        predict_label = predict(image, model)
        window_name = 'true: %s, predict: %s' % (gt_label, predict_label)
        plt.imshow(image[:, :, ::-1])
        plt.title(window_name)
        plt.show()


def demo_web():
    import requests
    import matplotlib.pyplot as plt
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    url = 'http://zhjwxk.cic.tsinghua.edu.cn/login-jcaptcah.jpg?captchaflag=login1'
    while True:
        r = requests.get(url)
        with open('demo.jpg', 'wb') as f:
            f.write(r.content)
        image = cv2.imread('demo.jpg')
        predict_label = predict(image, model)
        window_name = 'predict: %s' % predict_label
        plt.imshow(image[:, :, ::-1])
        plt.title(window_name)
        plt.show()



if __name__ == '__main__':
    # demo()
    demo_web()
