# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    col = input().split()
    
    total = 0
    for i in range(n):
        students = namedtuple('student', col)
        data = input().split()
        
        x = students(data[0],data[1],data[2],data[3])
        total += int(x.MARKS)
        
    print("{:.2f}".format(total/n))
