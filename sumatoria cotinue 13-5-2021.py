def sumatoria(i,n):
    result=i
    while i<=n:
        if(i%2)==0:
            i+=1
            continue
        #print(i)
        result+=i
        i+=1
    print(result)
        
def sumatoria1(i,n):
    result=i
    while i<=n:
        if(primo(i))==1:
            break 
        result+=i
        i+=1
    print(result)
        
