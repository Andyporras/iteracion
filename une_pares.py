def une_pares(lista):
    if(isinstance(lista,list)):
        if (verificar(lista)):
            pares=0
            while lista!=[]:
                n=lista[-1]
                if(n%2)==0:
                    largo=largo_aux(pares)
                    pares+=n*(10**largo)
                    lista=lista[:-1]
                else:
                    lista=lista[:-1]
                    
            else:
                return pares
        else:
            return "Error: contiene datos que no son enteros"
    else:
        return "Error."

def largo_aux(n):
    cont=0
    while n!=0:
        n=n//10
        cont+=1
    return cont
def verificar(lista):
    for n in lista:
        if(isinstance(n,int)and n>=0):
            continue
        else:
            return False
    return True

def es_especia(matriz):
    if(isinstance(matriz,list)):
        if(validar_aux(matriz)):
            if(validarTamaño(matriz))!=-1:
                if(fila_aux(matriz)==columna_aux(matriz[0])/2):
                    fila=fila_aux(matriz)
                    columna=columna_aux(matriz[0])//2
                    fila_actual=0
                    columna_Actual=0
                    matriz1=[]
                    matriz2=[]
                    suma1=[]
                    suma2=[]
                    while fila !=fila_actual:
                        if(columna_Actual==columna):
                            matriz1+=[suma1]
                            matriz2+=[suma2]
                            fila_actual+=1
                            columna_Actual=0
                            suma1=[]
                            suma2=[]
                        else:
                            
                            columna2=columna_Actual+columna

                        
                            suma1+=[matriz[fila_actual][columna_Actual]]
                            suma2+=[matriz[fila_actual][columna2]]
                        
                            columna_Actual+=1
                    fila=fila_aux(matriz)
                    columna=columna_aux(matriz[0])//2
                    fila_actual=0
                    columna_Actual=0
                    while fila !=fila_actual:
                        if columna_Actual==columna:
                            fila_actual+=1
                            columna_Actual=0
                        else:
                            comparar1=matriz1[fila_actual][columna_Actual]
                            comparar2=matriz2[columna_Actual][fila_actual]
                            if(comparar1==comparar2):
                                columna_Actual+=1
                            else:
                                return False
                    return True
                            
                else:
                    return "Error"
            else:
                return "Error2"
        else:
            return "Error"
    else:
        return "Error"
                        
                    
                
def validarTamaño(matriz):
    comparar=columna_aux(matriz[0])
    for lista in matriz:
        if(columna_aux(lista))==comparar:
            continue
        else:
            return False
    return True
            
def fila_aux(matriz):
    cont=0
    for lista in matriz:
        cont+=1
    return cont

def columna_aux(lista):
    cont=0
    for n in lista:
        cont+=1
    return cont
            

def validar_aux(matriz):
    for lista in matriz:
        if(isinstance(lista,list)):
            for n in lista:
                if(isinstance(n,int)):
                    continue
                else:
                    return False
            continue
        else:
            return False
    return True
                    
