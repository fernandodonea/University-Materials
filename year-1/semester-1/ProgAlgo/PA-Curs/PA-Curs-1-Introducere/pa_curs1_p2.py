x=7
print(x,id(x))
x=x+1
print(x,id(x))

x=100
z=0
y=z+100
print(id(x),id(y))
x=1000
z=0
y=z+1000
print(id(x),id(y))
x=1234567891234566923
print(x,type(x))

"""
x=0.1
print(x*x)
print(x*x==0.01) #False - precizie
print(abs(x*x-0.01)<1e-8) #True
"""