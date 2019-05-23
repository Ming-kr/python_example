# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:46:02 2019

@author: Ming
"""

import tensorflow as tf
import numpy as np

xy = np.loadtxt('data-01-test-score.csv' , delimiter=',' , dtype=np.float32)

x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

X = tf.placeholder(tf.float32,shape=[None,3])
Y = tf.placeholder(tf.float32,shape=[None,1])

W = tf.Variable(tf.random_normal([3,1]))
b = tf.Variable(tf.random_normal([1]))


hypothesis = tf.matmul(X,W) + b
cost = tf.reduce_mean(tf.square(hypothesis - Y)) #시그마.... 기울기 계산 아님... 코스트의 합....

train = tf.train.GradientDescentOptimizer(learning_rate = 0.00005).minimize(cost) #따라 내려가면서 최저 코스트 값 찾아 내겠다...

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(6001):
    cost_val,hv_val,_ = sess.run([cost,hypothesis,train],feed_dict={X: x_data, Y: y_data})
    
    if step%1000==0 or step < 5:
        print("오차 크기 : " , cost_val , "   기존값에 대한 예측 : " , hv_val )
        

while True:
    value1 = input("1 입력 종료=q>")
    if value1 == 'q':
        break

    value2 = input("2 입력 종료=q>")
    if value2 == 'q':
        break

    value3 = input("3 입력 종료=q>")
    if value3 == 'q':
        break

    
    listValue = []
    listValue.append(float(value1))
    listValue.append(float(value2))
    listValue.append(float(value3))
    
    tempList = []
    tempList.append(listValue)
    
    feed_dict = {X : tempList}
    result = sess.run(hypothesis,feed_dict)
    print("결 : ",result)
    















