# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    user_input = sorted(input())
    
    lower = ""
    upper = ""
    even = ""
    odd = ""
    for i in range(len(user_input)):
        if(user_input[i].isalpha()):
            if(user_input[i].isupper()):
                upper += user_input[i]
            else:
                lower += user_input[i]
        else:
            if(int(user_input[i])%2 == 0):
                even += user_input[i]
            else:
                odd += user_input[i]
                    
    print(lower,upper,odd,even, sep = "")
