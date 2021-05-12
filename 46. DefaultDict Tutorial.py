from collections import defaultdict

if __name__ == "__main__":
    n,m = map(int,input().split())
    a = defaultdict(list)
    b = []
    
    for i in range(1,n+1):
        temp = input()
        a[temp].append(i)
        
    for i in range(m):
        b += input()
            
    for i in range(m):
        if not a[b[i]]:
            print('-1')
            continue
        print(" ".join(map(str,a[b[i]])))
