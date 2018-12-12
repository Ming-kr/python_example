print("안녕하세요")
print("100")
print("%d 안ㄴ ... %s" %(100,"da"))

#표현식...
print("10진수 : %d 16진수 : %x 8진수 : %o .... %s 실수 : %f" %(100,100,100,"afasdfasf",0.1231))
print("정렬 기능.... %20d %20d %20s " %(100,200,"안녕하세요반갑습니다..."))

#문자열 .format

print("{0:d} {1:5d} {2:05d}".format(123,123,123))

#강제 행 바꿈... 특수 문자....자바 동일....
#행 안바꾸는 방법은?? 없나??;;;;;
print("adsfasf \n asdad")


#bool 타입 값 대문자 T임.... 아우 빡... False
#boolValue = True
#intValue = 10
#floatValue = 20.0
#strValue = "1231231"

#아래와 같이 사용 가능

boolValue,intValue,floatValue,strValue = False , 10 , 20.0 , "12321311"

print(boolValue)

#변수 타입 확인 가능...type 리턴 타입은 클래스...인가 보네.... 먼지 모르겠지만... 
print(type(boolValue))
print(type(intValue))

#예약어 종류
'''
True, False, None, and, or, not, break, continue, return, if, else, elif, for, while, except, finally, gloval, import, try 등
'''

#변수 종류 변경 가능 할까?
#되네..... 안 좋아.... 위험....
boolValue = "Asdfa"
print(boolValue)

# ; 는.... 한 줄 기준으로 명령어 나누는 기준인듯...
print(bin(11)) ; print(bin(0x11))

#3-4 예제
'''
sel = int(input("입력 진수 결정(16/10/8/2) : "))
num = input("값 입력 : ")

if sel == 16 :
    num10 = int(num, 16)
if sel == 10 :
    num10 = int(num, 10)
if sel == 8 :
    num10 = int(num, 8)
if sel == 2 :
    num10 = int(num, 2)
    
print("16진수 ==> ", hex(num10))
print("10진수 ==> ", num10)
print(" 8진수 ==> ", oct(num10))
print(" 2진수 ==> ", bin(num10))
'''

#**는 제곱인듯...
#int 형에는 크기 제한이 없음... 4바이트 아님...걍 정수형을 나타냄...
a = 100 ** 100
print(a)

#비트 값 쉽게 넣을 수 있음.... 좋다.... !!
b = 0b11011101101001010
b = 0o777
b = 0xFF
b = 255

#머..... 10진수 자리수 위
c = 3.14e3


#연산자.... 대부분... 자바랑 비슷... 특이한거 하나... // << 나눈후에 소수점 버리는 연산... 테스트 해보자...
#자바 int연산은 순수 정수.... 이녀석은 정수 기준이 아닌듯

a = 10
b = 20
result = a/b
print(result) #0.5로 나옴...

result = a//b
print(result) #0로 나옴...

#비교 연산자.. .결과는 boolean형.... 당연한 얘기....
a = (100 == 100)
print(a)
a = (300 < 200)
print(a)


a = "파이썬 만세"
a #이거 출력 안됨.....음.... 스크립트 모드에서는 안됨....대화형 모드에서만 가능
print(a)
type(a) #마찬가지....

#작은 따옴표 큰 따옴표 문법적으로 둘다 사용 가능 자바스크립트와 동일...
#예제 귀찮...

#근데....... """ << 이거 가능?????????? 먼 소리임...안되는데???? 안되는데??? 대화형 모드에서 먼가 되나보다...
#안되는데??? 안되는데???

#a = """asdfaf
#print(a)


#기본 데이터형??? __main__ << 예를 얘기하는듯.... 쓰레드 이름 이것지???

if __name__ == '__main__' :
    print(__name__)
    print(type(__name__))

###########################연산자#############################
#우선 순위 존재
#()로 연산자 우선순위 올릴수 있음...

#형 변환 int() , float() str()존재...
#대입 연산자 존재



#논리 연산자....and , or , not
a = (100 > 200) or (200 < 300)
a = not(a)

#아래와 같은 경우 가능
if(1231) : print(True)
if(0) : print(False)


#비트 연산자 존재...  << >> & | ^ ~


############################조건문############################
#파이썬은 들여쓰기가 매우 중요. if 문 다음에 ‘실행할 문장’은 if 문 다음 줄에서 들여쓰기를 해서 작성.
#들여쓰기 할 때는 Tab 보다 Space Bar 를 눌러 4칸 정도로 들여쓰기 권장,
#대화형 모드에서는 ‘실행할 문장’ 모두 끝나고 Enter  2번 눌러야 if 문이 끝나는 것으로 간주

#이건 머.....;;; 더 불편해 보인다....

a = 30
if a < 10 :
    print("a는 10보다 작다")
elif a < 20 :
    print("a < 20")
elif a < 40 :
    print("a < 40")
else :
    print("else")

fruit = ['사과','배','내가 좋아하눙 ~ 딸기','귤','큥~']

print(fruit)
fruit.append('큥큥~')
print(fruit)

if '배' in fruit:
    print('내가 시렇어하는 배가 있다')





    

































































