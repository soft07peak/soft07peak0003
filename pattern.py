num=int(input("enter a num:"))
for i in range (num,0,-1):
    for j in range (0,i):
        print ("*",end="")
    print ()
    
n=5
for i in range (n):
    for j in range (i,n):
        print ('',end='')
        
    for j in range (i+1):
        print ('*',end='') 
    print ()
n=5
for i in range (n):
    for j in range(i+1):
        print ('', end='')
        
    for j in range (i,n):
        print ('*', end='')
    print ()   
  