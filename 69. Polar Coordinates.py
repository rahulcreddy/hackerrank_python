# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

if __name__ == "__main__":
    z = input()
    z = complex(z)
    print(*cmath.polar(z), sep = "\n")
