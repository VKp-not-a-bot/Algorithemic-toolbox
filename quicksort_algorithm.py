


#print("enter numbers")
#s = input()
#num = list(map(int,s.split(' ')))
def swap(set,i,j):
    temp = set[i]
    set[i] = set[j]
    set[j] = temp

def pivot(set,first_number,last_number):
     i = first_number+1
     j = last_number
     while(i<j):
        print("i is " +str(i)+" and the value of j is "+str(j)+ " value of array is "+str(set))
        if(set[i]<set[first_number]):
            i+=1
        if(set[j]>set[first_number]):
            j-=1
        if(i>=j):
            print(str(i)+ "das is right")
            break
        if(set[i]>set[first_number] and set[j]<set[first_number]):
            swap(set,i,j)
            i+=1
            j-=1
     swap(set,0,i)
        
            


     print("i is " +str(i)+" and the value of j is "+str(j)+ " value of array is "+str(set))
"""""
def quicksort(set,a,b):
    if(length(set)==1):
        return null 
    p = pivot(set, a ,b)
    quicksort(set,a,p-1)
    quicksort(set,p+1,b)


    
    

"""
set = [7,1,5,2,3,6,4,13]
a = 0
b = 7
pivot(set,a,b)
