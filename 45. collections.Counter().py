from collections import Counter

if __name__ == "__main__":
    x = int(input())
    shoes_aval = Counter(map(int,input().split(" ")))
    n = int(input())
    
    earning = 0
    
    for i in range(n):
        size, price = map(int,input().split())
        if(shoes_aval[size] > 0):
            earning += price
            shoes_aval[size] -= 1
            
    print(earning)
