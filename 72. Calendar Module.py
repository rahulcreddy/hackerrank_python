# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__ == "__main__":
    day = list(map(int,input().split(" ")))
    x = calendar.weekday(day[2], day[0], day[1])
    print(calendar.day_name[x].upper())
