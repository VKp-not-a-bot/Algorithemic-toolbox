l =list(map(int,input().split(' ')))
w = l[0]
n = l[1]
weights = list(map(int,input().split(' ')))

weights.sort()
mat = [[0 for i in range(w+1)]for j in range(n+1)]
for i in range(n+1):
    
    
    for j in range(w+1):
        if(j==0):
            mat[i][j] =0
        elif(i==0):
            mat[i][j] = 0
        else:
            if(j-weights[i-1]>=0):
                
                mat[i][j] = max(mat[i-1][j-weights[i-1]]+weights[i-1],mat[i-1][j])
            else:
                mat[i][j] = mat[i-1][j]
print(mat[n][w])



