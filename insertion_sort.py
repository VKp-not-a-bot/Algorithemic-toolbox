l = [5,2,4,6,1,3]
def insertion(arr):
    i =1
    while(i<len(arr)):
        
        key = arr[i]
        j = i-1
        
        while(j>=0 and arr[j]>=key):
            
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
        i+=1
insertion(l)
print(l)

