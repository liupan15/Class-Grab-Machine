import tensorflow as tf
import scipy.io as sio
import numpy as np
from func import weight_variable
from func import bias_variable
from func import conv2d
from func import max_pool
from func import getbatch
import os

data1 = sio.loadmat('X.mat');
X = data1['X'];
data2 = sio.loadmat('y.mat');
y = data2['y'];
print('load data finished');

x = tf.placeholder("float", [None, 2500]);
y_actual = tf.placeholder("float", shape=[None, 62 * 5]);

x_image = tf.reshape(x, [-1, 25, 100, 1]);    # - 1表示根据x总的行数来定
W_conv1 = weight_variable([5, 5, 1, 32]);
b_conv1 = bias_variable([32]);
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1);
h_pool1 = max_pool(h_conv1);

W_conv2 = weight_variable([5, 5, 32, 64]);
b_conv2 = bias_variable([64]);
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2);
h_pool2 = max_pool(h_conv2);

W_fc1 = weight_variable([6 * 25 * 64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 6 * 25 *64])              #reshape成向量
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)    #第一个全连接层

#keep_prob = tf.placeholder("float") 
#h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)                  #dropout层

#W_fc2 = weight_variable([1024, 62 * 5])
#b_fc2 = bias_variable([62 * 5])
#y_predict=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)   #softmax层

#cross_entropy = -tf.reduce_sum(y_actual*tf.log(y_predict))     #交叉熵
#train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)    #梯度下降法
#ans = tf.argmax(y_predict,1);
#correct_prediction = tf.equal(ans, tf.argmax(y_actual,1))    
#accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))                 #精确度计算

#tf.summary.scalar('accuracy', accuracy);
#tf.summary.scalar('cross_entropy', cross_entropy);

sess=tf.InteractiveSession();

#merged_summary = tf.summary.merge_all();
#summarywriter = tf.summary.FileWriter('/tmp/', sess.graph);

sess.run(tf.global_variables_initializer())

for i in range(25000):
  print(i);
  
  batch = getbatch(X, y, 50);  #获取数据
  h_fc1.eval(feed_dict={x:batch[0], y_actual: batch[1]});
  #if i%100 == 0:                  #训练100次，验证一次
    #cross = cross_entropy.eval(feed_dict={x:batch[0], y_actual: batch[1], keep_prob: 1.0})
    #print('step',i,'training accuracy',cross)
    ##summary = sess.run(merged_summary, feed_dict={x:batch[0], y_actual: batch[1], keep_prob: 1.0});
    ##summarywriter.add_summary(summary, i);
  #train_step.run(feed_dict={x: batch[0], y_actual: batch[1], keep_prob: 0.5})


