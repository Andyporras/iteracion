def cotador():
    n=1
    while n<=10:
        print(n)
        n+=1
    else:
        print(f"fin del contador")

def sumatoria(n):
    result=0
    while n>0:
        result+=n
        n-=1
    return result


def sumatoria1(ini,fin):
    if(isinstance(ini,int)and isinstance(fin,int)and ini>=0 and fin>0):
        result=0
        while ini<=fin:
            result+=ini
            ini+=1
        return result
    else:
        return "ERROR, no cumple los parametro de entrada solicitado."

def largo(n):
    if(isinstance(n,int)):
        if(n==0):
            return 1
        elif(n<0):
            n*=-1
            result=0
            while n!=0:
                n=n//10
                result+=1
            return result
        result=0
        while n!=0:
            n=n//10
            result+=1
        return result
    else:
        return "ERROR, no cumple con el parametro solicitado."


#-------------------------------------------------------------------------------------------------------
    

def SumaVector(vector1,vector2):
    if(isinstance(vector1,list)and isinstance(vector2,list)and vector1!=[] and vector2!=[]):
        if(validar(vector1)):
            if(validar(vector2)):
                if(tamaño(vector1)==tamaño(vector2)):
                    result=[]
                    indice=0
                    
                    while indice<tamaño(vector1):
                        result+=[vector1[indice]+vector2[indice]]
                        indice+=1
                    return result

def tamaño(vector):
    cont=0
    while vector!=[]:
        cont+=1
        vector=vector[1:]
    return cont

def validar(vector):
    indice=0
    while indice <(tamaño(vector)):
        if(isinstance(vector[indice],int)):
            indice+=1
        else:
            return False
    return True
            
