n = int(input())
s = set(map(int, input().split()))
n_command = int(input())

for i in range(n_command):
    instruction = input().split()
    if(instruction[0] == 'pop'):
        eval("s.pop()")
    else:
        eval("s."+instruction[0]+"("+instruction[1]+")")
        
print(sum(s))
