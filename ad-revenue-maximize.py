# we are given two lists :- profit per ad clicks, and a list of slots whose no of clicks per day is known. My jobs is to bring in the
#sweet sweet $$ Kachinga
print("Enter the list of profits per ad click")
profit = list(map(int,input().split(' ')))
print("enter the list of average no of clicks per day for slots")
click =  list(map(int,input().split(' ')))
profit.sort(reverse=True)
click.sort(reverse=True)
i = 0
l = []
s = 0
for i in range(len(click)):
    l.append([profit[i],click[i]])
    s = s + profit[i]*click[i]
print(s)
print(l)
