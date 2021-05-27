# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    
    a = set(map(int,input().split()))
    n = int(input())
    
    result = 1
    for i in range(n):
        b = set(map(int, input().split()))
        
        if len(b.difference(a)) == 0:
            continue
        else:
            result = 0
            break
        
    if result:
        print("True")
    else:
        print("False")
