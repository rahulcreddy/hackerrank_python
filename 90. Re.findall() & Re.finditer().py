# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

if __name__ == "__main__":
    s = input()
    m = re.findall(r"(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})[bcdfghjklmnpqrstvwxyz]+", s, flags = re.I)
    print("\n".join(m or ["-1"]))
