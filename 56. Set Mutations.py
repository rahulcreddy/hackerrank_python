# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    a_num = int(input())
    a = set(map(int,input().split()))
    
    n = int(input())
    
    for _ in range(n):
        command = input().split()
        
        temp = set(map(int,input().split()))
        
        eval("a.{0}({1})".format(command[0],temp))
        
    print(sum(a))
