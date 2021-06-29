def matrizNulo(m):
    if(isinstance(m,list)):
        if(m!=[]):
            if(validar_tamaño(m)):
                if(validar_aux(m)):
                   return True
                else:
                   return False
            else:
                return "Error, tamaños distinto de los vectores"
        else:
            return "Error, matriz no debe ser una lista vacia"
    else:
        return f"Error. "

def validar_aux(m):
    while m!=[]:
        if(isinstance(m[0],list)):
            if(validarEntero(m[0])):
                m=m[1:]
            else:
                return False
        else:
            return False
    return True

def validarEntero(m):
    while m!=[]:
        if(m[0])==0:
            m=m[1:]
        else:
            return False
    return True
        
def validar_tamaño(m):
    v=m[0]
    while m!=[]:
        if(largo_Aux(m[0]))==largo_Aux(v):
            m=m[1:]
        else:
            return False
    return True
def largo_Aux(m):
    cont=0
    while m!=[]:
        m=m[1:]
        cont+=1
    return cont







    
        
