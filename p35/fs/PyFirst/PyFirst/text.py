x = "There are %d types of people." % 10
print(x)

binary = "binary"
doNot = "don't"

y = "Those who know %s and those who %s." % (binary, doNot)

print(y)

i = int(-5.7777)

print(i)

s = int("1231", 5)
print(s)

hello = None
res1 = hello is None
res2 = hello is not None
print(res1)
print(res2)

print(bool(0))
print(bool(123))
print(bool(-22))


a = 10
b = 4
z = a // b
print(z)
z = a / b
print(z)

myString = "hello " "world " "of " "Python"
print(myString)

sizes = ["small", "medium", "large", "x-large"]
for x in sizes:
    print(x)

print("-----------")
for i in range(len(sizes)):
    print(sizes[i])
    