# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    n = int(input())
    
    for i in range(n):
        text = input()
        print(re.sub(r"(?<= )(&&|\|\|)(?= )", lambda x: 'and' if x.group(1) == "&&" else "or", text))
