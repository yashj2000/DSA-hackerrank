n=int(input())
s=''
w=''
undo=['']
k=0

for i in range(0,n):
	choice=list(input().split())

	if int(choice[0])==1:
		w=choice[1]
		s=''.join((s,w))
		undo.append(s)
		
	elif int(choice[0])==2:
		k=int(choice[1])
		s = s[:(-k)]
		undo.append(s)

	elif int(choice[0])==3:
		k=int(choice[1])-1
		print(s[k])

	elif int(choice[0])==4:
		undo.pop()
		s=undo[-1]