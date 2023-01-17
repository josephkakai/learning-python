myint = 10
myfloat = 10.25
mystr = "kaks the boss"
mybool = True
mylist = ["chai", "ugali", "githeri","nyama"]
mydict = {"kenya":1964, "Tanzania": 1960, "Uganda": 1956, "SouthAfrica":1990}
mytuple = ("kupika", "kukula", "kuitika", "kuosha")

print(mydict)
print(mystr)
print(mytuple)
print(myfloat)
print(myint)
print(mybool)
print(mylist)
print(type(mybool))


myint = 11
myfloat = 11.5
mystr = "joe kaks is the new boss"
mybool = False
mylist = ["githu muigai", "nancy baraza", "johnson sakaja"]
mytuple = ("ghana", "nigeria", "morocco","china")
mydict = {"jomo kenyatta": 1964, "nelson mandela": 1995, "julius nyarere": 1960}


print(mydict["jomo kenyatta"])
# print(mystr)
print(mytuple[2])
# print(myfloat)
# print(myint)
# print(mybool)
print(mylist[1])
print(mylist[0:2])
print(mylist[::-1])

print("this is a string" + str(123))
def someFunction():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)

del mystr
print(mystr)

