


print("enter numbers")
s = input()
num = list(map(int,s.split(' ')))



def swap(set,i,j):
    temp = set[i]
    set[i] = set[j]
    set[j] = temp

def pivot(set,first_number,last_number):
     i = first_number+1
     j = last_number
     while(i<j):
        
        #print("i is " +str(i)+" and the value of j is "+str(j)+ " value of array is "+str(set)+" fist number is "+str(first_number)+" last number is "+str(last_number))
        if(set[i]<=set[first_number]):
            i+=1
        if(i>=j):
           # print(str(i)+ "das is right")
            break
        if(set[j]>=set[first_number]):
            j-=1
        if(i>=j):
           # print(str(i)+ "das is right")
            break
        if(set[i]>set[first_number] and set[j]<set[first_number]):
            swap(set,i,j)
            i+=1
            j-=1
        if(i>=j):
           # print(str(i)+ "das is right")
            break
     if(i== first_number+1):
        if(set[i]<set[first_number]):
            swap(set,first_number,i)
            
            return i
        else:
            
            return i
            
     else:
        if(set[first_number]>set[i]):
           swap(set,first_number,i)
           return i
        else:
            swap(set,first_number,i-1)
            return i-1

        
        


     
    
def quicksort(set,first,last):
    
    #print("first = "+str(first)+" last is "+ str(last)+" the string is "+str(set))
    if(first==last):
        
        return 0
    p = pivot(set,first,last)
    #print(p)
    
    
    if(p==first):
        quicksort(set,p+1,last)
    elif(p==last):
        quicksort(set,first,p-1)
    else:
        quicksort(set,first,p-1)
        quicksort(set,p+1,last)

#print(pivot(s,0,2))
quicksort(num,0,len(num)-1)
#print(pivot(s,0,5))
print(num)




