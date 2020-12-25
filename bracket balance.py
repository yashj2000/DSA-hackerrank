querries=int(input())
i=0
flag=0
s=str()
stack=[]
for i in range(querries):
    s=input()
    for x in s:
        if x=='(' or  x=='[' or x=='{':
            stack.append(x)
        else:
            if not stack:
                flag=1
            else:
                z=stack.pop()
                if x==')':
                    y='('
                elif x==']':
                    y='['
                else:
                    y='{'
                if z!=y:
                    flag=1
        print(stack)

    if flag==1:
        print('NO')
        flag=0
    elif x in stack:
	    print('NO')
	    flag = 0
    else:
        print('YES')
