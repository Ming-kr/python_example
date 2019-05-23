import numpy as np
import matplotlib.pyplot as plt
import random

#학습용 값
plt.scatter([1,2,3,5,6,7] , [10,20,30,50,60,70])



#가설에 해당하는 그래프의 변화

x = np.arange(0, 10, 0.1) #0에서 10까지 0.1 간격으로 데이터 생성
print(type(x))
w = int(random.random()*20)
b = int(random.random()*20)
y = w*x + b   # 생성된 데이터를 sin 함수를 이용하여 y에 할당함

plt.plot(x,y)   # x,y 값으로 그래프를 그림

w = int(random.random()*20)
b = int(random.random()*20)
y = w*x + b
plt.plot(x,y)

plt.show()      # 그려진 그래프를 화면에 출력
