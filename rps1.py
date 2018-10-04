import random

a=('r','p','s')

s1=0
s2=0

c=random.choice(a)

a=input("enter value r/p/s:")
		print("you choose a and computer choose c")
	while True:
			if(a==c)
				print("it is a tie")
			elif(a==r and c==s)
				print("you won",a beats c)
				s1=1
			else:
				print("computer wins")	
			elif(a==s and c==p)
				print("you win"a cuts c)
				s1=1
			else:
				print("computer wins")
			elif(a==p and c==r)
				print("you won"a covers c)
				s1=1
			else:
				print("computer wins")
			elif(a==p and c==s)
				print("c won",c cuts a)
				s2=1
			else:
				print("you wins")
			elif(a==r and c=p)
				print("c wins",c covers a)
				s2=1
			else:
				print("you wins")
			elif(a==s and c==r)
				print("c won",c beats r)
				s2=0
			else:
				print("you wins")
			if(s1=3)
				print("you are champ","s1",:,"s2")
			else:
				print("c wins")
			if(s2=3)
				print("coputer is champ","s1",:,"s2")
			else:
				print("you wins")
			break
