[n,m],array,A,B = map(int,input().split()),map(int,input().split()),set(map(int,input().split())),set(map(int,input().split()))
my_happiness = 0
for num in array:
    if num in A:
        my_happiness+=1
    elif num in B:
        my_happiness-=1
print(my_happiness)
