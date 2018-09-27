import random
print("hello")
count=0
while(count<=100):
		n=input("enter r to roll a dice")
		if (n=='r'):
			r=random.randint(1,6)
			print("r value is",r)
			count=count+r
			print("score is",count)
			if(count==100):
				print("u won")
				print("your score is",count)
			elif(count==11):
				count=2
				print("oops u have snake byte")
			elif(count==8):
				count=37
				print("hurray you have climb up a ladder")
			elif(count==13):
				count=34
				print("hurray you have climb up a ladder")
			break