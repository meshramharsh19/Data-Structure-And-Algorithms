s = "erase*****"
ans = []
for ch in s:
    if ch != '*':
        ans.append(ch)
    else:
        ans.pop()
return(str(''.join(ans)))