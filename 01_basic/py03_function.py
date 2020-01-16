"""
python 函数的参数传递：

    1、不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
    2、可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
"""


"""不可变变量传参"""
def test(parm):
    parm =  parm + 1
    print(parm)

parm = 1
test(parm)
print(parm)



"""可变变量传参"""
def testList(list):
    list.append(4)
    print(list)

list = [1,2,3]
testList(list)
print(list)



"""局部里定义global全局变量"""
def func():
    global x
    print(x)
    x = 2

x = 1
func()
print(x)



"""关键参数
    实参和形参使用相同变量名字（关键字）可调整调用函数的参数位置
"""
def func(a, c=10):
    print('a is', a,'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)




"""默认参数值"""
def say(message, times = 1):
    print(message * times)

say('Hello')
say('World', 5)



"打印任何传入的参数"
def printinfo( arg1, *vartuple ):
   print(arg1)
   for var in vartuple:
      print(var)
      
printinfo( 10 );
printinfo( 70, 60, 50 );