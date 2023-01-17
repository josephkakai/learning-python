def func1():
    print("i am being tested by kakai")

def func2(arg1, arg2):
    print(arg1, "" , arg2)

def cube(x):
    return x*x*x

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

def multiadd(*args):
    result = 0
    for x in args:
        result = result + x
    return result

func1()
print(func1())
print(func1)
func2(10, 20)
print(10, 20)
cube(3)
print(cube(3))
print(cube(10))
print(power(2))
power(2)
print(power(2,3))
print(power(x=3,num=2))
print(multiadd(3))
print(multiadd(4,2,5,2,4))