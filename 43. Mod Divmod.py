# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    num = int(input())
    den = int(input())
    print(num//den)
    print(num%den)
    print(divmod(num,den))
