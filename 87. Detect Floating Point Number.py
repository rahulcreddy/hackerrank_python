# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        print(bool(re.match(r"^[+-]?[0-9]*\.[0-9]+$", input())))
