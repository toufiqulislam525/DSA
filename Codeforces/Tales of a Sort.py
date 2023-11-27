n = int(input())
result = [0] * n
for i in range(n):
    sz = int(input())
    if sz > 0 :
        l = [int(j) for j in input().split()]
        max = []
        max.append(0)
        count = 1
        for (ind,v) in enumerate(l):
            if(count == 1):
                count-=1
                continue
            if(v >= l[max[-1]]):
                max.append(ind)
        
        tempsz = sz-1
        maxid = max[-1]
        
        while(tempsz == maxid and tempsz > 0):
            max.pop()
            tempsz-=1
            maxid = max[-1]

        if(maxid == 0 and tempsz == 0):
            result[i] = 0
        else:
            result[i] = l[maxid]

        

for i in result:
    print(i)
        
    
    