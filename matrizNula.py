def matrizNula(m):
    if(isinstance(m,list)):
        if(m!=[]):
            if(columna_aux(m)):
                if(validar(m)):
                    return True
                else:
                    return False
            else:
                return "Error: sus vectores no son de igual tamaño"
        else:
            return "Error: matriz vacia"
    else:
        return 'Error tipo de dato, no es matriz'

def validar(m):
    while m!=[]:
        if(isinstance(m[0],list)):
            if(validarCero(m[0])):
                m=m[1:]
            else:
                return False
        else:
            return False
    return True

def validarCero(m):
    while m!=[]:
        if(m[0]==0):
            m=m[1:]
        else:
            return False
    return True

def columna_aux(m):
    comparar=columna_Aux(m[0])
    while m!=[]:
        if(columna_Aux(m[0]))==comparar:
            m=m[1:]
        else:
            return False
    return True

def columna_Aux(m):
    cont=0
    while m!=[]:
        m=m[1:]
        cont+=1
    return cont
