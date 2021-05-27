# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    m = int(input())
    temp = input().split()
    n = int(input())
    temp2 = input().split()
    first_set = set(temp) 
    second_set = set(temp2)

    m = first_set.difference(second_set)
    n = second_set.difference(first_set)
    
    p = m.union(n)
    print ("\n".join(sorted(p, key = int)))
