# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    x, k = map(int,input().split())
    poly = input()
    res = eval(poly)
    
    if(res == k):
        print("True")
    else:
        print("False")
