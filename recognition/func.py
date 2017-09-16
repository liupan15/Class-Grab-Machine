import tensorflow as tf
import numpy as np
import random


def weight_variable(shape):    #初始化权值 W
    initial = tf.truncated_normal(shape, stddev = 0.1);  # 0.1
    return tf.Variable(initial);

def bias_variable(shape):     #初始化偏置 b
    initial = tf.constant(0.1, shape = shape);
    return tf.Variable(initial);

def conv2d(x, W):            # 构建卷积层
    return tf.nn.conv2d(x, W, strides = [1,1,1,1], padding = 'SAME');

def max_pool(x):            #池化
    return tf.nn.max_pool(x, ksize=[1,2,2,1],strides=[1,1,1,1],padding='SAME');

def getbatch(X, y, num):
    seed = 7;
    np.random.seed(seed);
    batchx = np.zeros((num, 2500));
    batchy = np.zeros((num, 62 * 5));
    for i in range(num):
        tmp = int(random.random() * 300);
        batchx[i, :] = X[tmp, :];
        batchy[i, :] = y[tmp, :];
    return [batchx, batchy];
