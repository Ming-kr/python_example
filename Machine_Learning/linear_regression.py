#선형 회귀

import tensorflow as tf

X = [1,2,3,5,6,7]
Y = [10,20,30,50,60,70]
#W = tf.Variable(tf.random_normal([1]))  #기울기를 따라 내려가기만 하면됨... 어디 위치든... 그래서 랜덤... 직접 값 줘도 될듯
#b = tf.Variable(tf.random_normal([1]))  #기울기를 따라 내려가기만 하면됨... 어디 위치든... 그래서 랜덤... 직접 값 줘도 될듯 [0] = 스칼라 , [1] = 벡터 , [2] = 집합
#W = tf.Variable(10.0) #코스트가 0가 되는 경우
#b = tf.Variable(0.0) #코스트가 0가 되는 경우.....

W = tf.Variable(1.0)
b = tf.Variable(0.0)


hypothesis = W * X + b
#hypothesis = W * X
cost = tf.reduce_mean(tf.square(hypothesis - Y)) # square = 제곱(음수 없애기) , reduce_mean = 시그마 , 모든 오차의 값 합 이후 내기

print("cost : " , cost)

#아래 두줄... 0.01만큼씩 기울기를 따라서 내려간다... 결론 최저 코스트 값 찾기....
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01) #테스트 결과 0.5부터는 튕겨 나감.....
train = optimizer.minimize(cost)

sess = tf.Session()

sess.run(tf.global_variables_initializer()) #global_variables_initializer = Variable 값들 실직적으로 이때 세팅...

print(":::::",type(sess.run(W)),sess.run(b))

print("===== 학습 연산 과정 =====")

for step in range(2001):
    sess.run(train)
    if step % 200 == 0 or step < 5:
        print(step,sess.run(cost),sess.run(W),sess.run(b))

print("===값 입력 테스트===")
while True:
    inputValue = input("몇시간 공부 했습니까?(종료=q)>")  
    if inputValue == "q":
        break
    hypothesis = W * int(inputValue) + b
    print(sess.run(hypothesis))









