#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import S
from pyparsing import empty


print ('hello world')

# classmates = ['Michael', 'Bob', 'Tracy']
# classmates.

def findMinAndMax(L):
    if L:

        min = L[0]
        max = L[0]
        for i in L:
          if min>i:
              min = i
          if max<i:
              max = i
        return(min,max)
    else:
        return (None, None)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

#生成器
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

#map/reduce
def normalize(name):
    for i in name:
        
    pass

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#filter
# 练习
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    n = str(n)
    a = n[::-1]
    if a == n:
        return a
        
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

#sorted
# 练习
# 假设我们用一组tuple表示学生名字和成绩：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    name=[]
    for n in t:
        name.append(str.lower(n))
        return name

L2 = sorted(L, key=by_name)
print(L2)

# 再按成绩从高到低排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_score(t):
    score = []
    for n in range(len(t)):
        score.append(L.pop(n)[1])
        return score

L2 = sorted(L, key=by_score ,reverse=True)
print(L2)

# 返回函数
# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数

def createCounter():
    n = 0
    def counter():
        nonlocal n
        n = n + 1
        return n
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


# 关键字lambda表示匿名函数
# 练习
# 请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))

L = list(filter(lambda x : x % 2 == 1,range(1,20)))

print(L)

# 装饰器
# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time, functools

def metric(fn):
    def usetime(*arg,**kw):
        t = time.time()
        ret = fn(*arg,**kw)
        print('%s executed in %s ms' % (fn.__name__, time.time() - t))
        return ret
    return usetime
# 测试
@metric
def fast(x, y):
    time.sleep(1.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# 偏函数