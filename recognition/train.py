import cv2
import numpy as np
from glob import glob
import scipy.io as sio

s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
filename = glob('./images300/*.jpg');

X = np.zeros((300, 2500));
y = np.zeros((300, 62 * 5));

for i in range(0, 300):
    img= cv2.imread(filename[i]);
    #cv2.namedWindow('233')
    #cv2.imshow('233', img);
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);
    img = cv2.resize(img, (25, 100));
    img = img / 255;
    img = np.reshape(img, (1, 2500));
    X[i, :] = img;
    label = filename[i].split('\\')[-1].split('.')[0]
    lens = len(label);
    for j in range(lens):
        tmp = s.find(label[j]);
        y[i, tmp + j * 62] = 1;
        
print(X);
print(y);
sio.savemat('X.mat', {'X':X});
sio.savemat('y.mat', {'y':y});
