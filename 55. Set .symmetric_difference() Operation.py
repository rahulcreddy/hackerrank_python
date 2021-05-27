# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    m = int(input())
    eng = input().split()
    n = int(input())
    fre = input().split()
    
    e = set(eng)
    f = set(fre)
    
    print(len(e^f))
