a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print('|',a[0],'|',a[1],'|',a[2],'|')
	print("-----------")
	print('|',a[3],'|',a[4],'|',a[5],'|')
	print("-----------")
	print('|',a[6],'|',a[7],'|',a[8],'|')	
playerOneTurn=True
while True:
	printboard()
	p=input("choose available place:")

	if(p in a):
		if(a[int(p)-1]=='x' or a[int(p)-1]=='0'):
			print("place taken,choose another place:")
			continue
		else:
			if playerOneTurn:
				print("Player 1 >>")
				a[int(p)-1]='x'
				playerOneTurn=not playerOneTurn
			else:
				print("Player 2 >>")
				a[int(p)-1]='0'
				playerOneTurn=not playerOneTurn
			for i in(0,4,8):
				if(a[i]==a[i-1] and a[i]==a[i-2]):
					print("game over");
					exit()
			for i in range(3):
				if(a[i]==a[i-3] and a[i]==a[i-6]):
					print("game over")
					exit()
			for i in(0,4,8):
				if(a[i]==a[i-1] and a[i]==a[i-5]):
					print("game over")
					exit()

	else:
		continue


| 1 | 2 | 3 |
-----------
| 4 | 5 | 6 |
-----------
| 7 | 8 | 9 |
choose available place:4
Player 1 >>
| 1 | 2 | 3 |
-----------
| x | 5 | 6 |
-----------
| 7 | 8 | 9 |
choose available place:5
Player 2 >>
| 1 | 2 | 3 |
-----------
| x | 0 | 6 |
-----------
| 7 | 8 | 9 |
choose available place:3
Player 1 >>
| 1 | 2 | x |
-----------
| x | 0 | 6 |
-----------
| 7 | 8 | 9 |
choose available place:4
| 1 | 2 | x |
-----------
| x | 0 | 6 |
-----------
| 7 | 8 | 9 |
choose available place:6
Player 2 >>
| 1 | 2 | x |
-----------
| x | 0 | 0 |
-----------
| 7 | 8 | 9 |
choose available place:7
Player 1 >>
| 1 | 2 | x |
-----------
| x | 0 | 0 |
-----------
| x | 8 | 9 |
choose available place:2
Player 2 >>
| 1 | 0 | x |
-----------
| x | 0 | 0 |
-----------
| x | 8 | 9 |
choose available place:8
Player 1 >>
| 1 | 0 | x |
-----------
| x | 0 | 0 |
-----------
| x | x | 9 |
choose available place:9
Player 2 >>
| 1 | 0 | x |
-----------
| x | 0 | 0 |
-----------
| x | x | 0 |
choose available place:1
Player 1 >>
game over
