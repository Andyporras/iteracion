def contarDigitos(n):
    if(isinstance(n,int)):
        cont=0
        while n >=0:
            if(n==0):
                return cont
            n=n//10
            cont+=1
        return cont

    else:
        return 'Error tipo de dato'
