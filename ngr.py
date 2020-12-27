a=list(map(int,input().split()))
ans=[]
stack=[]
def ngr(a):
	a=a[::-1]
	for i in a:
		if not stack:
			ans.append(-1)
			stack.append(i)
		elif stack[-1]>=i:
			ans.append(stack[-1])	
			stack.append(i)		
		elif stack and stack[-1]<=i:
			while stack and stack[-1]<=i:
				stack.pop()

			if not stack:
				ans.append(-1)
				stack.append(i)
			else:
				ans.append(stack[-1])
				stack.append(i)

	print(ans[::-1])
ngr(a)