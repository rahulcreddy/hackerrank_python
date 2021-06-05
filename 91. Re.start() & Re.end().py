# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == "__main__":
    s = input()
    k = input()
    
    m = re.search(k,s)
    pat = re.compile(k)
    
    if not m:
        print("(-1, -1)")
    while m:
        print("({0}, {1})".format(m.start(),m.end()-1))
        m = pat.search(s,m.start()+1)
