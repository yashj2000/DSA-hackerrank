l1 = list(map(int, input().split()))
stack = []
ans = []
s = []
for i in l1:
    if not stack:
        ans.append(-1)
        s.append(-1)
        stack.append(i)
    else:
        if stack[-1] >= i:
            ans.append(stack[-1])
            s.append(l1.index(ans[-1]))
            stack.append(i)                 #jo bhi ans me append hoga uska index l1 
                                            #wali list me se S wali list me dalo
        else:
            while stack and stack[-1] <= i:
                stack.pop()
            if not stack:
                ans.append(-1)
                s.append(-1)
            else:
                ans.append(stack[-1])
                s.append(l1.index(ans[-1]))
            stack.append(i)
# print(ans)
# print(s)

final=[i-s[i] for i in range(0,len(s))]

print(final)