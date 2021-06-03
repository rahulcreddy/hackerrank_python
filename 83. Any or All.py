if __name__ == "__main__":
    N = int(input())
    num = input().split()
    
    print(all([int(i) > 0 for i in num]) and any([i == i[::-1] for i in num]))
