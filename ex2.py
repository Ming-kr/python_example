# 주석

'''
여러줄 주석 
'''

print("첫번째 값을 입력하세요 : ")
inputValue1 = input()
print("두번째 값을 입력하세요 : ")
inputValue2 = input()

result = int(inputValue1) + int(inputValue2)

print("두 값의 합 : " , result)

############## 아마도 import 나중에 넣어도 될듯 #############

import turtle
turtle.shape('turtle')
for i in range(0,5) :
    turtle.forward(200) #거리 것지...
    turtle.right(72) #각도 인듯...

turtle.done()
