# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    k = int(input())
    a = input().split()

    single = set()
    multi = set()

    for i in a:
        if i in single:
            multi.add(i)
        else:
            single.add(i)
            
    print((single.difference(multi)).pop())
