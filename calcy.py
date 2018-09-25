def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mult(a,b):
	return(a*b)
def divide(a,b):
	return(a/b)

i=int(input("enter value of a:"))
j=int(input("enter value of b:"))
o=input("what do you want to do?+,-,*,/:")

if(0=='+'):
	res=add(i,j)
if(0=='-'):
	res=sub(i,j)
if(0=='*'):
	res=mult(i,j)
if(0=='/'):
	res=divide(i,j)

print(res)