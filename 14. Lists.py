if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        arg = input().strip().split(" ")
        if arg[0]!="print":
            arg[0]+="("+",".join(arg[1:])+")"
            eval("l."+arg[0])
        else:
            print(l)
