if __name__ == '__main__':
    records = []
    scores = set()
    out_name = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.add(score)
        
    second_lowest = sorted(scores)[1]
    
    for name, score in records:
        if score == second_lowest:
            out_name.append(name)
            
    for name in sorted(out_name):
        print(name,end='\n')
