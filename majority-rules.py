n = int(input())
set = list(map(int,input().split(' ')))
def cnt(set,maj,n):
    i = 0
    count =0
    while(i<n):
        if(set[i]==maj):
            count+=1
        i+=1
    return count

def true(first,last,left,right,set):
    i = first
    countl = countr =0
    while(i<=last):
        if(set[i]==left):
            countl+=1
        elif(set[i]==right):
            countr+=1
        i+=1
    tot = last-first+1

    if(countr>tot/2):
        return right
    elif(countl>tot/2):
        return left
    else:
        return None

def majority(first,last,set):
    if(first==last):
        return set[first]

    
    mid = (first+last)//2
    left = majority(first,mid,set)
    right = majority(mid+1,last,set)
    if(left==right):
        return left
    elif(left!=None and right == None):
        return left
    elif(right!=None and left == None):
        return right
    elif(right!=None and left != None and left != right):
        return true(first,last,left,right,set)
    elif(right==None and left ==None):
        return None

maj = majority(0,n-1,set)

if(cnt(set,maj,n)>n/2):
    print(1)
else:
    print(0)
    

