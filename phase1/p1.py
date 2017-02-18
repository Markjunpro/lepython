
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
name=input('please enter you name: ')
print('hello',name)

#print absolute value of an integer:
a=100
if a>=0:
    print(a)
else:
    print(-a)

'''
from pyclbr import Class

'''
#if else
#int(str)
age_str=input('please enter you true age:')
age=int(age_str)
print("the age_str is equal:",age_str)
print("the age is equal is age",age)
if age>=18:
    print('adult')
else:
    print('teenager')
'''

'''
# formatting
lastyear_scord_str=input('please enter you lastyear_scord :')
lastyear_scord=int(lastyear_scord_str)
if lastyear_scord<0 or lastyear_scord>100:
    input('lastyear_scord is invaild,please enter again:')
thisyear_scord_str=input('please enter you thisyear_scord :')
thisyear_scord=int(thisyear_scord_str)
if thisyear_scord < 0 or thisyear_scord > 100:
    input('thisyear_scord is invaild,please enter again:')
true_rate=(thisyear_scord-lastyear_scord)/lastyear_scord
print('scord growth rate:%d %%' %true_rate)
base_rate=5
if true_rate>base_rate:
    print("great scord growth")
else:
    print('no any growth')
'''


'''
#if 条件判断
age=3
if age>=18:
    print('your age is :',age)
    print('adult')
elif age>6:
    print('kid')
else:
    print('your age is :',age)
    print('teenager')
'''



'''
#计算bmi:身高除以体重的平方
xiaoming_height_str=input('hi,xiaoming,please enter your true height by m :')
xiaoming_height=float(xiaoming_height_str)
if xiaoming_height<=0:
    input('your height is invaild ,please enter your true height by m :')
xiaoming_weight_str=input('hi,xiaioming,please enter your weight:')
xiaoming_weight=float(xiaoming_weight_str)
if xiaoming_weight<=0:
    input('your weight is invaild,pleae enter your true weight by kg:')
xiaoming_bmi_1=xiaoming_weight/xiaoming_height
xiaoming_bmi=xiaoming_bmi_1/xiaoming_height
print(xiaoming_bmi)
if xiaoming_bmi>32:
    print('严重肥胖')
elif xiaoming_bmi>28 and xiaoming_bmi<=32:
    print('肥胖')
elif xiaoming_bmi>25 and xiaoming_bmi<=28:
    print('过重')
elif xiaoming_bmi>18.5 and xiaoming_bmi<=25:
    print('正常')
else:
    print('过轻')
'''


#循环
# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
'''
names=['Michael','Bob','Tracy']
for name in names:
    print(name)
'''

'''
sum=0
for x in range(101):
    sum=sum+x
print(sum)
'''

'''

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
'''


'''
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello',name)

'''



'''
#定义函数
在Python中，定义一个函数要使用def语句，
依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。
请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。

'''


'''
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
test=my_abs("a")
print(test)
'''



'''
#空函数
def nop():
    pass

'''
'''
参数检查

调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
>>> my_abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: my_abs() takes 1 positional argument but 2 were given

但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别：
>>> my_abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in my_abs
TypeError: unorderable types: str() >= int()
>>> abs('A')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
'''

''''
#返回多个值
#-*- coding=utf-8 -*-

import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
r=move(100,100,60,math.pi/6)
print(r)

'''


'''
# 计算一元二次方程的解
#-*- coding=utf-8 -*-
import math
a_str=input('please enter a :')
b_str=input('please enter b :')
c_str=input('please enter c :')
a=float(a_str)
b=float(b_str)
c=float(c_str)
'''
'''
def quadratic(a, b, c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise typeError("a is not int or float")
    x=(-b+math.sqrt(b*b-4*a*c))/2*a
    y=(-b-math.sqrt(b*b-4*a*c))/2*a
    return x,y
x,y=quadratic(2,3,1)
print(x,y)
'''
'''
#位置参数

def power(x):
    return x*x
print(power(5))
print(power(15))
'''
'''
def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5,2))
print(power(5,3))
'''
'''
#默认参数
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5))

'''
'''
def enroll(name,gender,age=6,city='beijing'):
    print('name :',name)
    print('gender :',gender)
    print('age :',age)
    print('city :',city)
#enroll('mark','F')
#enroll('bob','F',7)
enroll('mark','F',city='wuhan')
'''
'''可变参数

在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下
'''
'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1,2,3]))
'''


#位置参数：一个参数
#默认参数：多个参数，设置默认值
#可变参数：参数的个数可变，tuple


#关键字参数:多个参数名


'''
def person(name,age,**kw):
    print('name :',name,'age :',age,'other :',kw)
extra={'city':'beijing','job':'Engineer'}
#person('Mark',30,city=extra['city'],job=extra['job'])
person('Mark',30,**extra)
'''


'''
#关键字命名参数
def person(name,age,*,city,job):
    print(name,age,city,job)
person('jack',24,city='beijing',job='engineer')
'''

'''
#参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

'''
def f1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
print(f1(1,2))
'''

#递归函数
'''在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。'''
'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(100))
#递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
'''


'''
L=[]
n=1
while n<=99:
    L.append(n)
    n=n+2
print(L)
'''

#迭代
#在Python中，迭代是通过for ... in来完成的

'''
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
'''

'''
list:    d=[1,2,3]
tuple:   d=(1,2,3)
dict:    d={1,2,3}
'''


'''
d={'a':1,'b':2,'c':3}
for k,v in d.items():
    print(k,v)
'''

'''
for ch in 'ABC':
    print(ch)

'''

'''
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
'''


'''
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['A','B','C']):
    print(i,value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
'''

'''
#list comprehensions
x=list(range(1,11))
print(x)
'''

'''
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)
'''


'''
x=[x*x for x in range(1,11) if x % 2==0]
print(x)
'''

'''
y=[m+n for m in "ABC" for n in "XYZ"]
print(y)

'''


'''
import os
Z=[d for d in os.listdir('.')]
print(Z)
'''

'''
#list
L=[x*x for x in range(1,10)]
print(L)


#generator
g=(x*x for x in range(1,10))
for n in g:
    print(n)

'''

'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        a,b=b,a+b
        n=n+1
    return 'done'
print(fib(5))
'''


'''
#!/usr/bin/env python3
#-*- coding=utf-8 -*
'a test module'
__author__ = 'Michael Liao'
import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,world')
    if len(args)==2:
        print('Hello,%s!' % args[1])
    else:
        print('Too Many arguments!')

if __name__=='__main__':
    test()
'''

'''
def _private_1(name):
    return 'Hello,%s' % name
def _private_2(name):
    return 'Hi,%s' % name
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
t=greeting('mark')
print(t)

'''


'''
开头有双下划线    ==》》  私有变量（外部不可访问）
开头和结尾都有双下划线  ==》》 特殊变量（外部可访问）
开头单下划线  ==》》  视为私有变量（不建议访问）
若要访问，可在class内部单独添加函数
'''

class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')
mark=Student('Mark.li',99)
print(mark.get_name(),'%s' % mark.get_score())
