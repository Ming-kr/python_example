# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:46:02 2019

@author: Ming
"""

import tensorflow as tf

x_data = [[10.,20.], [30.,12.], [25.,35.], [32.,40.]]
y_data = [[5.],[7.],[10.],[12.]]

X = tf.placeholder(tf.float32,shape=[None,2])
Y = tf.placeholder(tf.float32,shape=[None,1])

W = tf.Variable(tf.random_normal([2,1]))
b = tf.Variable(tf.random_normal([1]))


hypothesis = tf.matmul(X,W) + b
cost = tf.reduce_mean(tf.square(hypothesis - Y)) #시그마.... 기울기 계산 아님... 코스트의 합....

train = tf.train.GradientDescentOptimizer(learning_rate = 0.0001).minimize(cost) #따라 내려가면서 최저 코스트 값 찾아 내겠다...

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(6001):
    cost_val,hv_val,_ = sess.run([cost,hypothesis,train],feed_dict={X: x_data, Y: y_data})
    
    if step%1000==0 or step < 5:
        print("오차 크기 : " , cost_val , "   기존값에 대한 예측 : " , hv_val )
        

while True:
    value1 = input("중간 고사 점수 입력 종료=q>")
    if value1 == 'q':
        break

    value2 = input("기말 고사 점수 입력 종료=q>")
    if value2 == 'q':
        break
    
    listValue = []
    listValue.append(float(value1))
    listValue.append(float(value2))
    
    tempList = []
    tempList.append(listValue)
    
    feed_dict = {X : tempList}
    result = sess.run(hypothesis,feed_dict)
    print("장학금 : ",result)
    















