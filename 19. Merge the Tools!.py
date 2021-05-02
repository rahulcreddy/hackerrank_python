def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        sub_str = string[i:i+k]
        char_seen = []
        for char in sub_str:
            if char not in char_seen:
                char_seen.append(char)
        print(''.join(char_seen))
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
