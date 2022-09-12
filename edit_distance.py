s1 = input()
s2 = input()

a = len(s1)
b =len(s2)

mat = [[0 for _ in range(a+1)] for _ in range(b+1)]


#the following code defines the edit distance algorithm in this block of code
for i in range(b+1):
    
    for j in range(a+1):
        
       
        

        if(i==0 ): 
            mat[i][j] = j
        elif(j==0):
            
            mat[i][j] = i
        else:
            if(s1[j-1]==s2[i-1]):
                x = mat[i-1][j-1]
                mat[i][j] = x
            else:
                x = mat[i-1][j-1]+1
                mat[i][j] = min(mat[i][j-1]+1,mat[i-1][j]+1,x)

print(mat[b][a])


