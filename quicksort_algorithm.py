



def partition(first,last,set):
    i= first
    part = first
   
    while(i<last):
        if(set[i]<=set[last]):
            set[i],set[part] = set[part],set[i]
            part+=1
        i+=1
    set[last],set[part] = set[part],set[last]
    return part
def quicksort(first,last,set):
    if(first==last):
        return None
    p = partition(first,last,set)
    if(p==first):
        quicksort(p+1,last,set)
    if(p==last):
        quicksort(first,p-1,set)
    else:
        quicksort(first,p-1,set)
        quicksort(p+1,last,set)

n = list(map(int,input().split(' ')))

quicksort(0,len(n)-1,n)
print(n)

