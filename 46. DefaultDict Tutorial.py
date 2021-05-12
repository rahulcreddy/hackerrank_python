from collections import defaultdict

if __name__ == "__main__":
    n,m = map(int,input().split())
    a = defaultdict(list)
    
    for i in range(1,n+1):
        a[input()].append(str(i))
            
    for i in range(m):
        b = input()
        if b in a:
            print(" ".join(a[b]))
        else:
            print("-1")
