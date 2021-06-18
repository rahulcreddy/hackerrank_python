cube = lambda x: x**3# complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    start = [0,1]
    for i in range(2,n):
        start.append(start[i-1] + start[i-2])
    return start[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
