if __name__ == '__main__':
    data = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name,score])
    scores = [st[1] for st in data]
    min_score = min(scores)
    count = scores.count(min_score)
    while count>0:
        scores.remove(min_score)
        count-=1
    min_score = min(scores)
    names = []
    for i in data:
        if(i[1]==min_score):
            names.append(i[0])
    names.sort()
    print(*names,sep="\n")
