list1=[-1,2,3,-4,10,-5,34]
x=list(i for i in list1 if i>=0)
print(x)
y=list(i*i for i in x )
print(y)
a=list(input('Enter the name'))
v=['a','e','i','o','u']
b=list(i for i in a if i in v )
print(b)
print(ord('G'))
