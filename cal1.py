n = int(input())
def dynamic(n):
 l = [0,0]
 a =0
 b=0
 c =0
 another = [0,0]

 for i in range(2,n+1):
     a=100000000
     b=100000000

     j = l[i-1]+1
     l.append(j)
     another.append(1)
     
     
     if(i%2==0):
         a = l[i//2]+1
         l[i] = min(j,a)
         
         if(min(j,a)==j):
             another[i]=1
         elif(min(j,a)==a):
             another[i] = 2
         
     if(i%3==0):
         b = l[i//3]+1
         l[i]= min(j,a,b)
         
         if(min(j,a,b)==a):
             another[i] = 2
         elif(min(j,a,b)==j):
             another[i] = 1
         elif(min(j,a,b)==b):
             another[i]=3
         
     
     
     
 k = n
 ans =[n]
 while(k>1):
     
     if(another[k]==1):
         ans.append(k-1)
         k=k-1
     elif(another[k]==2):
         ans.append(k//2)
         k = k//2
     elif(another[k]==3):
         ans.append(k//3)
         k = k//3
 ans.sort()

 print(l[n])
 print(*ans,' ')
dynamic(n)



    