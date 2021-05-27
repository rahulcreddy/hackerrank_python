# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        a_num = int(input())
        a = set(map(int,input().split()))
        b_num = int(input())
        b = set(map(int, input().split()))
        
        if len(a.difference(b)) == 0:
            print("True")
        else:
            print("False")
