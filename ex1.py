Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello world~!!!")
hello world~!!!
>>> 10 + 29
39
>>> 
>>> a=100
>>> b=200
>>> print(a+b)
300
>>> print(a + b + '안녕하세요')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a + b + '안녕하세요')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(a+'안' + b)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(a+'안' + b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> println(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    println(a)
NameError: name 'println' is not defined
>>> print(a,"안녕하세요",b)
100 안녕하세요 200
>>> print(a,'녕하세요',b)
100 녕하세요 200
>>> 
