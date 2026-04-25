s = '2[a]3[ab]'
stack = []
current_string = ''
num = 0

for ch in s:
    if ch.isdigit():
        num = num * 10 + int(ch)
    
    elif ch == '[':
        stack.append((current_string, num))
        current_string = ''
        num = 0
    
    elif ch == ']':
        prev_String, repeat = stack.pop()
        current_string = prev_String + repeat * current_string
    
    else:
        current_string += ch

print(current_string)