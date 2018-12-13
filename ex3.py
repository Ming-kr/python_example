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

#대화형이라 .... 중간에 import 해도 됨....
import random

numbers = []
for num in range(0,10,1):
    numbers.append(random.randrange(0,100))

print("랜덤 값들 : ",numbers)


#출력과 값 입력을 동시에 가능 함...
#test = input("값을 입력하세요 : ")



########################반복문######################

#for i in range(3):
#for i in range(0,3):
for i in range(0,3,1):
    print("안녕하세요")

#foreach 문.....
for i in [0,1,2]:
    print("반갑습니다")


#파이썬 for문 팁... 사용하지 않는 i는 _로(변수임) 사용... 명명법

#while문과 for문의 확실한 분리...

for i in range(2,10):
    print("=======%d단=======" %i)
    for x in range(1,10):
        print("%d X %d = %d" %(i,x,i*x))

test = 0

while True :
    test += 1
    if test > 10:
        break

    if test%2==0:
        continue
    
    print("while문.. True")
    

print("\u2665")


###################자료 구조 (리스트,튜플,딕셔너리)##################
#파이썬은 아예 문법으로 자료구조를 제공함...
#최대 핵심.... 파이썬 존재의 이유....

aa = [10,2,3,4,"asdad",3.455]

print(aa[4])

aa = [] #빈 리스트 생성 ... 확실히 자료 구조 인듯...
aa.append(10)
aa.append(10)
aa.append("113sad")
aa.append(10)
aa.append(10)

print(aa[2])

print("리스트 카운트 :" , len(aa))

#print(aa[10])

for i in aa:
    print("test aa : " , i)

bb = aa[1:3] #범위 지정 인덱스 1부터 3이전까지 인듯....

print("test :",bb)

print("test - :",bb[-1]) #음수 값으로 접근 가능 ... 뒤에부터...

print(aa[2:]) #2번 부터...
print(aa[:2]) #2번 이전 까지...

aa += aa #리스트 끼리 연산 가능...빼기도 되나??
#aa -= aa #안됨
print(aa)

aa *= 3 #똑같은것 3개... 붙임...
print("======")
print(aa)

print("======")
bb = aa[::2]
print(bb) #2개씩 건너뛰어 만들기...
bb = aa[::-2]
print(bb) #뒤에서 부터 2개씩 건너뛰어 만들기...

bb = aa[:] #복사

print("======")
aa[1:3] = [200,300,11,111,23,3]  #중간 값 변경...
#대박.... 꼭 일치 하지 않아도...알아서 맞추는듯... 아니다... 이건 머냐!!!
#위에 범위를 지우고 새로운 내용을 끼워 넣는다....
print(aa)


###슬슬 먼가 이상함.... 이거 메모리 구조가 어떻게 되는거지?????
## aa[1:3] << 이 경우 복사생성후 메모리 리턴 구조 아닌가????

print("=================test================")

print(aa)
del(aa[0]) #???????? 무엇을 근거로 지는거??
#값? 참조 주소?? append가 있으면 지는것도 있을텐데....
#우선 값은 아닌듯...
aa.remove(10)
aa.remove(10)
aa.remove(10)
aa.remove(10) #이 녀석이 값으로 지우네... 근데 하나만 지움... 먼가 방법이 있겠지...
print(aa)

aa[1:4] = [] #인덱스 1~3까지 삭제....

aa = None # null인듯....

########################리스트 API 예제###################
print("########################리스트 API 예제###################")
myList = [30, 10, 20]
print("현재 리스트 : %s" % myList)
myList.append(40)
print("append(40) 후의 리스트 : %s" % myList)
print("pop()으로 추출한 값 : %s" % myList.pop())
print("pop() 후의 리스트 : %s" % myList)
myList.sort() #정렬은 무엇을 기준으로??? 그리고 기준 정할 수 있나??
print("sort() 후의 리스트 : %s" % myList)
myList.reverse()
print("reverse() 후의 리스트 : %s" % myList)
print("20값의 위치 : %d" % myList.index(20))
myList.insert(2, 222)
print("insert(2, 222) 후의 리스트 : %s" % myList)
myList.remove(222)
print("remove(222) 후의 리스트 : %s" % myList)
myList.extend( [77, 88, 77] ) # + 하고 기능 동일....
print("extend([77, 88, 77]) 후의 리스트 : %s" % myList)
print("77값의 개수 : %d" % myList.count(77))
newList = myList.copy() #복사 생성...


###그외... API###
del(myList[1]) ##위치값 지움....혹은...#myList[1] = []
print(len(myList))
newList = sorted(myList) #기존 리스트는 놔두고 새로운 리스트 소트해서 생성...


###########튜플#########
#튜플 생성..... ( )로 생성...
#읽기 전용....

tt1 = (10,20,30)
tt2 = 10,20,30 #이렇게도됨...
tt3 = 10, #항목이 하나인 튜플... 혹은 (10,)
nottt4 = (10) #이건 튜플 아닌듯...
print(type(tt3))
print(type(nottt4))

del(tt3) #튜플 삭제....
print(tt1[1]) #접근
#접근은 리스트와 비슷함... 범위 포함...
#튜플도 더하기 곱하기 됨.... 새로운 투플 만드니까 그렇겠지??

#튜플 리스트로 변환
myList = list(tt1)

##########딕셔너리#########
#해쉬맵....임....순서대로 안들어감...

dic1 = {'s001':1111,'s002':2222,'s003':3333}

print(dic1['s001'])
print(dic1.get('s001'))

dic1['s001'] = 1234

del(dic1['s002'])


print(dic1.keys()) ##얜 리턴 타입이 머냐?????? 리스트 인듯....튜플인가??
print(type(dic1.keys())) ##dict_keys 타입이네.... 어쨌든 list(dic1.keys())로 변환 가능...















































































