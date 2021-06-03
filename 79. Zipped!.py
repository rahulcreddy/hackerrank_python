# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n, x = map(int,input().split())

    sub = []
    for _ in range(x):
        sub.append(map(float,input().split()))
           
    for i in zip(*sub):
        print(sum(i)/len(i))
