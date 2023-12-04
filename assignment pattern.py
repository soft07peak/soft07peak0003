n=int(input("enter a num:"))
for i in range (n):
    for j in range (n-i-1):
        print ("",end=" ")
    for j in range (2*i+1):
        print ("*",end="")
    print ()  

for i in range ( n-1):
    for j in range (i+1):
        print ("",end=" ")
    for j in range (2*(n-i-1)-1):
        print ("*", end="")
    print ()  
    
    
n=int(input("enter a number:")) 
for i in range (n,0,-1):
    for j in range (n-i):
        print (" ",end=' ')
    for j in range ( 1,2*i):
        print ("*",end=' ')  
    print ()   
    
for i in range (2,n+1) :
    for j in range (n-i):
        print (" ",end=' ')
    for j in range (1,2*i):
        print ("*", end=' ')  
    print ()   
    
    
n=int(input("enter a number:"))  
i=n
while (i > 0):
    j = i
    while (j > 0):
        if i == 1 or i == n or j == 1 or j ==i:
            print ('*',end = '')
        else:
            print (' ', end = '')   
        j = j - 1  
    i = i - 1
    print ()  
     
n=int(input("enter a number:"))  
for i in range (n):
    for j in range (n-i):
        print (' ', end='')
    for j in range (2*i+1) :
        if j==0 or j==2*i or i==n-1:
            print ('*', end='')
        else:
            print (' ', end='')   
    print ()       