# abs() : absolute value

import math
x = -5
y = -0.005
print(abs(x))  # 5
print(abs(y))  # 0.005

# all() : return true if all iterables are true or iterable is empty

w = []  # True
x = [1, 2, 3]  # True
y = [True, True, True]  # True
z = [True, False, True]  # False
a = [False, False, False]  # False
b = [0, 1, 2, 3]  # False
print(all(w))
print(all(x))
print(all(y))
print(all(z))
print(all(a))
print(all(b))

# any() : return true if any of the iterable is true. False if empty

print(any(w))  # False
print(any(x))  # True
print(any(y))  # True
print(any(z))  # True
print(any(a))  # False
print(any(b))  # True

# ascii() : return string containing printable representation of an object

str = "G ë ê k s f ? r G ? e k s"
print(ascii(str))  # 'G \xeb \xea k s f ? r G ? e k s'

# bin(): convert an int to binary string prefixed with "0b".

print(bin(3))  # 0b11
print(bin(-10))  # -0b1010

print(format(14, '#b'))  # 0b1110
print(format(14, 'b'))  # 1110

print(f'{14:#b}')  # 0b1110
print(f'{14:b}')  # 1110

# bool() : converted using the 'truth test procedure'

w = 1  # True
x = 0  # False
y = 3  # True
z = 'me'  # True
a = ''  # False
b = input  # True
c = [[1, 2], [z, a]]  # True
d = []  # False

print(bool(w))
print(bool(x))
print(bool(y))
print(bool(z))
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))


# bytearray(source, encoding, errors) : returns a byte array

str = "GeeksforGeeks"
array1 = bytearray(str, 'utf-8')  # bytearray(b'GeeksforGeeks')
# bytearray(b'\xff\xfeG\x00e\x00e\x00k\x00s\x00f\x00o\x00r\x00G\x00e\x00e\x00k\x00s\x00')
array2 = bytearray(str, 'utf-16')
size = bytearray(3)  # bytearray(b'\x00\x00\x00')
array3 = bytearray(b"abcd")  # bytearray(b'abcd')
array4 = bytearray(b'aaaacccc')  # bytearray(b'aaaacccc')
list1 = bytearray([0, 3, 5, 6])  # bytearray(b'\x00\x03\x05\x06')
# list2 = bytearray([555, 666, 777]) # ValueError: byte must be in range(0, 256)

print(array1)
print(array2)
print(size)
print(array3)
for val in array3:
    print(val)
print(array4)
print("Count of c is:", array4.count(b'c'))
print(list1)

# bytes(source, encoding, errors) : returns an immutable byte object

byte1 = bytes(str, 'utf-8')
byte2 = bytes(str, 'utf-16')

print(byte1)
print(byte2)

for val in byte2:
    print(val)

# callable(object) : returns true if object is callable, false otherwise


class callMe:
    def __init__(self):
        self.x = 5


print(callable(5))  # False
print(callable(print))  # True
print(callable(bytes))  # True
print(callable(callMe))  # True

# chr(i) : returns the string representation of the integer i. ord() is the inverse

print(chr(97))  # a
print(chr(1999))  # ߏ
print(chr(8933))  # ⋥

# @classmethod : let's us call a function using the class name instead of object instance


class c:
    x = 5

    def __init__(self):
        self.x = 0

    @classmethod
    def callUs(cls):
        print(cls.x)

    def callMe(self):
        print(self.x)


c.callUs()  # 5
b = c()
b.callMe()  # 0

# compile(source, filename, mode, flags, dont_inherit=False, optimize=-1) : returns a code object from source (string, byte string, AST object).
# The returned object can be executed with exec() - sequence of statements
# OR eval() - single expression
# OR single() - single interactive statement

source = 'print("Im here")'
sourceCode = compile(source, 'string', 'exec')
exec(sourceCode)  # Im here

source = '''
j = 5
for i in range(j):
    print(i, end=',' )
print()'''

sourceCode = compile(source, 'anystring', 'exec')
exec(sourceCode)  # 0,1,2,3,4,

# complex([real[, imag]])

z1 = complex(2, -3)  # (2-3j)
z2 = complex(1)  # (1+0j)
z3 = complex()  # (0j)
z4 = complex('5-9j')  # (5-9j)
z5 = z1 + z4  # (7-12j)

print(z1, z2, z3, z4, z5)

# delattr(object, name) : deletes objects attribute (name) if allowed


class c:
    attr1 = "1"
    attr2 = "2"
    attr3 = "3"


b = c()
print(b.attr1)  # 1
delattr(c, 'attr1')
# print(b.attr1)  # ! 'c' object has no attribute 'attr1'
b.attr1 = '5'
print(b.attr1)  # 5
b.fakeattr = '8'  # dynamic creating property?
print(b.fakeattr)  # 8


# dict
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(a == b == c)  # True

# dir() : print list of modules and variables in namespace

print(dir())  # ['__annotations__', '__builtins__', '__cached__', '__doc__',
# ' __file__', '__loader__', '__name__', '__package__', '__spec__',
# 'a', 'array1', 'array2', 'array3', 'array4', 'b', 'byte1', 'byte2', 'c', 'callMe', 'd',
# 'i', 'j', 'list1', 'size', 'source', 'sourceCode', 'str', 'val', 'w', 'x', 'y', 'z', 'z1', 'z2', 'z3', 'z4', 'z5']

print(dir(math))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan',
# 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees',
# 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod',
# 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite',
# 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2',
# 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh',
# 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

print(dir(c))  # ['__class__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
# '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys',
# 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# divmod(a,b) : returns pair (a // b, a % b)

a = 6
b = 3
c = 4
res1 = divmod(a, b)  # (2,0)
res2 = divmod(a, c)  # (1,2)
print(res1)
print(res2)

# enumerate(iterable, start=0) : (index, value) pair

letters = ['a', 'b', 'c', 'd']

for index, value in enumerate(letters):  # (0,a), (1,b), (2,c), (3,d), (4,e)
    print(f"({index},{value}) ")
print(list(enumerate(letters)))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

# eval(expression[,globals[,locals]]) : expression is parsed and evaluated as a python expression

x = 4
# 'expressions' are values (static code execution), not like statements which can 'do' things
expression = 'x+1'
print(eval(expression))  # 5

# exec(object[,globals[.locals]] : support dynamic execution of code
x = 6
expression = '''
for i in range(5):
    print(i)
print(x)
x = 3
print(x)'''
exec(expression)  # 0 1 2 3 4 6 3

# filter(function, iterable) : construct iterator for those elements of iterable which function returns true.

x = [True, True, True, False]
for index, value in enumerate(filter(None, x)):
    print(index, value)  # 0 True 1 True 2 True
x = [1, 2, 3, 4, 5, 6, 7]
for index, value in enumerate(filter(lambda y: y % 2 == 0, x)):
    print(index, value, end=', ')  # 0 2, 1 4, 2 6
print()

# float (x) : return a float from a number or string
print(float(5))  # 5.0
print(float('-123'))  # -123.0
print(float('+1E6'))  # 1000000.0
print(float('-Infinity'))  # -inf

# format(value[,format_spec]) : returns a formatted string
# -- format spec:  [[fill]align][sign][#][0][width][,][.precision][type] -- #

pi = 3.14
# [fill]align[sign][width]
print(format(pi, '0>10'))  # 0000003.14
print(format(pi, '0<10'))  # 3.14000000
print(format(pi, '&^10'))  # &&&3.14&&&
print(format(pi, '&^+10'))  # &&&+3.14&&&
print(format(pi, '&=+10'))  # +&&&&&3.14

print(format(pi, '&=+10.4f'))  # +&&&3.1400
print(format(97, 'c'))  # a
print(format(95, 'x'))  # 5f
print(format(95, 'X'))  # 5F
print(format(0.88, '.2%'))  # 88.00%

# frozenset(iterable) : creates immutable object from iterable
a = [1, 2, 3, 4, 5]
a[2] = 9
frozen = frozenset(a)  # frozenset({1, 2, 4, 5, 9})
print(frozen)
# frozen[2] = 6 - Error!

# getattr(object,name[,default]) : return the value of the named attribute of object


class c:
    attr1 = "1"
    attr2 = "2"
    attr3 = "3"


print(getattr(c, 'attr2'))  # 2

# globals() : return a dictionary of current global symbol table

print(globals())
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000000F4CECD9C88>,
# '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'BuiltIns.py', '__cached__': None, 'math': <module 'math' (built-in)>,
# 'x': [1, 2, 3, 4, 5, 6, 7], 'y': 3, 'w': 1, 'z': 'me', 'a': [1, 2, 9, 4, 5], 'b': 3, 'str': 'GeeksforGeeks', 'c': <class '__main__.c'>, 'd': [], 'array1': bytearray(b'GeeksforGeeks'),
# 'array2': bytearray(b'\xff\xfeG\x00e\x00e\x00k\x00s\x00f\x00o\x00r\x00G\x00e\x00e\x00k\x00s\x00'), 'size': bytearray(b'\x00\x00\x00'), 'array3': bytearray(b'abcd'), 'array4': bytearray(b'aaaacccc'),
# 'list1': bytearray(b'\x00\x03\x05\x06'), 'val': 0, 'byte1': b'GeeksforGeeks', 'byte2': b'\xff\xfeG\x00e\x00e\x00k\x00s\x00f\x00o\x00r\x00G\x00e\x00e\x00k\x00s\x00', 'callMe': <class '__main__.callMe'>,
# 'source': "\nj = 5\nfor i in range(j):\n    print(i, end=',' )\nprint()", 'sourceCode': <code object <module> at 0x000000F4D07830C0, file "anystring", line 2>, 'j': 5, 'i': 4, 'z1': (2-3j), 'z2': (1+0j),
# 'z3': 0j, 'z4': (5-9j), 'z5': (7-12j), 'res1': (2, 0), 'res2': (1, 2), 'letters': ['a', 'b', 'c', 'd'], 'index': 2, 'value': 6, 'expression': '\nfor i in range(5):\n    print(i)\nprint(x)\nx = 3\nprint(x)',
# 'pi': 3.14, 'frozen': frozenset({1, 2, 4, 5, 9})}

# hasattr(object, name)
print(hasattr(c, 'attr1'))  # True
print(hasattr(c, 'attr5'))  # False

# hash(object) : takes an object and returns a hashed value
print(hash(4))  # 4
print(hash('Hash Me'))  # 8171030424018843618
print(hash('123'))  # 6900734044072233614
print(hash('Hash Me'))  # 8171030424018843618

# help(object) : intended for interactive use.
# help() - starts up interactive help console

# hex(x) : convert int to lowercase hex
print(hex(255))  # 0xff
print(hex(-42))  # -0x2a

print(float.hex(1.23))  # 0x1.3ae147ae147aep+0

# id(object) : return the 'identity' of an object - unique and constant during the lifetime of the object
print(id(c))  # 179468742888
print(id(c))  # 179468742888

# input(prompt) : read line from input - prompt argument is added to stdout
# s = input()  # stdin
# s = input('===>')  # ===> stdin
