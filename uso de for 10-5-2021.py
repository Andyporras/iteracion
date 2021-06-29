def usoFor_range():
    for num in range(1,11):
        print(num)
    print("fin")

def usoFor_range_v2():
    for num in range(1,11,3):
        print(num)
    print("fin")
    
def usoFor_range_v3():
    for num in range(100,10,-10):
        print(num)
    print("fin")

    
    
def sumatoriaFor(i,n):
    suma=0
    for num in range(i,n+1):
        suma+=num
    print(f"el resultado de la sumatoria es:{suma}")

def enteroPrimo(n):
    result=False
    for num in range(2,n+1):
        if(num==n):
            result=True
        elif(n%num)==0:
            break
        else:
            num
    return result



            
