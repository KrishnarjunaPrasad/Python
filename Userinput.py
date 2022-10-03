'''
x=int(input("Enter 1st numnber:"))
y=int(input("Enter 2st numnber:"))
res = x&y
print("Result:",res)
'''


'''
x = input("Enter any char: ")
a=x[0]
print(a)
##print(x[0])
'''




'''x = input("Enter any char: ")
count = len(x)
print(count)
'''


'''
x = input("Enter any char: ")
if len(x)!= 1:
    print("Enter only one char:")
    x = input("Enter any char: ")
    print(x)
else:
    print(x)
'''


x = input("Enter any char: ")
while len(x)!= 1:
    print("Enter only one char:")
    x = input("Enter any char: ")
    print(x)
else:
    print(x)
