# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
if __name__ == "__main__":
    S = input()
    
    print(*[(len(list(group)),int(key)) for key,group in groupby(S)])
