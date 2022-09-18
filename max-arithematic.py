s = input()

def matprint(mat,r,c):
    for i in range(r):
        print(mat[i])
    
def oper(num1,num2,op):
    if(op == '+'):
        return num1+num2
    elif(op == '*'):
        return num1*num2
    elif(op == '-'):
        return num1-num2

def sep(s):
    x = []
    y=[]
    a =""
    for i in range(len(s)):
        if(s[i]=='+' or s[i]=='-' or s[i]=='*' ):
            x.append(s[i])
            y.append(int(a))
            a = ''
            
        else:
            a = a+s[i]
    y.append(int(a))
    return [x,y]
x = sep(s)
numbers = x[1]
operators = x[0]
num = len(numbers)
BigM = [[0 for i in range(num)] for j in range(num)]
m = [[0 for i in range(num)] for j in range(num)]
i =0
j =0 
for k in range(num):
    i =0
    while(j<num):
        if(i==j):
            BigM[i][j] = numbers[i]
            m[i][j] = numbers[i]
        else:
            temp1 = temp2 =-10000000
            for t in range(j-i):
                temp1 = max(oper(BigM[i][i+t],BigM[i+t+1][j],operators[i+t]),oper(BigM[i][t+i],m[i+t+1][j],operators[i+t]),oper(m[i][t+i],BigM[t+1+i][j],operators[i+t]),oper(m[i][t+i],m[t+1+i][j],operators[i+t]))
               
                    
                if(temp1>=temp2):
                    temp2= temp1
            BigM[i][j] = temp2
            temp3 = temp4 = 10000000
            for t in range(j-i):
                temp3 = min(oper(BigM[i][i+t],BigM[i+t+1][j],operators[i+t]),oper(BigM[i][t+i],m[i+t+1][j],operators[i+t]),oper(m[i][t+i],BigM[t+1+i][j],operators[i+t]),oper(m[i][t+i],m[t+1+i][j],operators[i+t]))
              
                    
                if(temp3<=temp4):
                    temp4= temp3
            m[i][j] = temp4

        i+=1
        j+=1       
    j = k+1
print(BigM[0][num-1])
    
        

