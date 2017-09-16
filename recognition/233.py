import scipy.io as sio
import scipy
import numpy as np
import cv2

s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
data1 = sio.loadmat('Theta1.mat');
Theta1 = data1['Theta1'];

data2 = sio.loadmat('Theta2.mat');
Theta2 = data2['Theta2'];

img = cv2.imread('./images300/22HW.jpg');   # read & show the picture

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY);

img = cv2.resize(img, (25, 100))
img = img / 255;

img = np.reshape(img, (1, 2500));

tmp1 = np.ones((1, 2501));

tmp1[0, 1:2501] = img;

h1 = Theta1.dot(tmp1.T);

#print(h1.shape);

h1 = 1 / (1 + np.exp(-h1));

tmp2 =np.ones((1, 26));
tmp2[0, 1 : 26] = h1.T;

#print(tmp2);

h2 = Theta2.dot(tmp2.T);
h2 = 1 / (1 + np.exp(-h2));
h2 = np.reshape(h2,(5, 62));
#print(h2);
string = '';
for i in range(4):
    index = np.argmax(h2[i, :]);
    string = string + s[index];
if(np.max(h2[4, :]) > 0.1):
    index = np.argmax(h2[4, :]);
    string = string + s[index];
print(string);
