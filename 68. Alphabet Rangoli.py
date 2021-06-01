import string

def print_rangoli(size):
    # your code goes here
    al = string.ascii_lowercase
    out = []
    for i in range(size):
        s = "-".join(al[i:size])
        out.append((s[::-1] + s[1:]).center(4*size-3,"-"))
    print('\n'.join(out[:0:-1]+out))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
