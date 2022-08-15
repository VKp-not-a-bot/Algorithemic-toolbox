n = int(input())
set = list(map(int,input().split(' ')))
m = int(input())
srch = list(map(int,input().split(' ')))
def binary_search(set,key,first,last):
    if(set[first]==key):
        return first
    if(set[last]==key):
        return last
    
    
    elif(first==last-1 ):
        return -1
    else:
        mid = (first+last)//2
        
        if(set[mid]==key):
            return mid
        elif(key>set[mid]):
            return binary_search(set,key,mid,last)
        elif(key<set[mid]):
            return binary_search(set,key,first,mid)
#l= [1,5,8,12,13]
#print(binary_search(l,11,0,4))

ans = []
for i in range(m):
    ans.append(binary_search(set,srch[i],0,n-1))
print(*ans , sep = ' ')


