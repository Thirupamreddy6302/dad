print("welcome to game ")
s1=0
s2=0
while(s1<=3 or s2<=3):
		a=input("enter r as rock p as  paper s as scissor ")
		import random
		d=['r','p','s']
		s=random.choice(d)
		print(s) 
		if (a==s):
			print("draw ,,,,,")
			print(s1)
			print(s2)
		elif(s1==3):
			print("you won the game")
			break
		elif(s2==0):
			print("you lose the game")
			break
		elif (a=='p'and s=='r'):
			print("point")
			s1=s1+1
			print(s1)
			print(s2)
		elif (a=='p'and s=='s'):
			print("point")
			s1=s1+1
			print(s1)
			print(s2)
		elif (a=='s'and s=='r'):
			print("point")
			s1=s1+1
			print(s1)
			print(s2)
		elif (a=='s'and s=='p'):
			print("point")
			s1=s1+1
			print(s1)
			print(s2)
		elif (a=='r'and s=='s'):
			print("point")
			s1=s1+1
			print(s1)
			print(s2)
		elif (a=='r'and s=='p'):
			print("point")
			s1=s1+1
			print(s1)
			print(s2)

OUTPUT:
welcome to game 
enter r as rock p as  paper s as scissor r
r
draw ,,,,,
0
0
enter r as rock p as  paper s as scissor r
s
you lose the game
