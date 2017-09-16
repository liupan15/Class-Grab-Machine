#!/usr/bin/env python
import cv2
import numpy as np
from glob import glob
import pickle


def train():
    images_fname = glob('./images300/*.jpg')
    num_image = len(images_fname)
    assert num_image == 300
    feature = np.zeros((num_image, 3780))
    label = list()
    for image_idx in range(num_image):
        image_ = cv2.imread(images_fname[image_idx])
        label_ = images_fname[image_idx].split('/')[-1].split('.')[0]  # get the label
        feature_ = cv2.HOGDescriptor()
        feature_ = feature_.compute(cv2.resize(image_, (64, 128)))[:, 0]
        feature[image_idx, :] = feature_
        label.append(label_)
    with open('model.pkl', 'wb') as f:
        pickle.dump({'feature': feature, 'label': label}, f)
    print('Model saved to model.pkl')


if __name__ == '__main__':
    train()
