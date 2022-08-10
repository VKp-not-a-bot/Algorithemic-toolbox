print("enter the distance")
d = int(input())
print("enter milage")
mil = int(input())
print("enter refilling stops")
stops = list(map(int,input().split(' ')))
travel =0
def closest(a,b):
    i = 0
    for i in  range(len(b)):
        b[i] = b[i] - a
    
    return max([i for i in range(len(b)) if b[i] <= 0])
count = 0
pits = []

i =0
cpy = stops.copy()
#print(stops[closest[775,cpy]])

while(i<10):
    cpy = stops.copy()
    travel = travel+mil
    if(travel>d):
        break
    index = closest(travel,cpy)
    travel = stops[index]
    count+=1
    pits.append(stops[index])
    print(travel)
    i+=1
print(count)
print(pits)

