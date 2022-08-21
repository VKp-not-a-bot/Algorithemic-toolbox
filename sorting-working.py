# Uses python3
import sys
import random

             



def partition3(a, l, r):
    #write your code here
    pass

def partition2(a, l, r):
  #  print("the string coming into partition is"+str(a))
    x = a[l]
    j = l
    var = l+1
    count =1
    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            a[i], a[j] = a[j], a[i]
        if a[i] == x:
            
            a.insert(var,x)
            a.pop(i+1)
            var+=1
            j+=1
            
            count+=1
    
    for num in range(0,count):
         a.insert((j+1),x)
    for num in range(0,count):
        a.pop(var-count)
  #  print("the string going out is "+str(a))
    

    return [j-count+1,j]


def randomized_quick_sort(a, l, r):
  #  print("the string in quick sort"+str(a)+" whose first number is "+ str(l)+" last number is "+str(r))
    
    
    if l >= r:
        return
    if(l<=r):
     k = random.randint(l, r)
    # print("the random number is "+ str(k))
     a[l], a[k] = a[k], a[l]
    
     m = partition2(a, l, r)
     #print(m)
     #print("the value f partition is "+ str(m))
     if(m[0]==l):
         randomized_quick_sort(a, m[1] + 1, r)
     if(m[1]==r):
         randomized_quick_sort(a, l, m[0] - 1)
     else:
         randomized_quick_sort(a, l, m[0] - 1)
         randomized_quick_sort(a, m[1] + 1, r)



    
    


n = int(input())
#n = 100
#a = []
#a = [4,2,7,7,5,4,3,4]
a = list(map(int, input().split()))
#for i in range(0,n):
   # a.append(random.randrange(0,10))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')
