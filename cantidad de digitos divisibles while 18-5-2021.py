"""
nombre:cantidadDigitosDivisibles
entrada: numero= un numero entero positivo
digitoDivisor= numero entero positivo
salida: cantidad de numero divisibles, del numero entre digitoDividor

"""
def cantidadDigitosDivisibles(numero,digitoDividor):
    if(isinstance(numero,int)and isinstance(digitoDividor,int)and(numero>0)):
        if digitoDividor<10 and digitoDividor>0 :
            cont=0
            while numero >0:
                if(numero%10)%digitoDividor==0:
                    numero=numero//10
                    cont+=1
                else:
                    numero=numero//10
            print(f"cantidad de digitos divisibles {cont}")
        else:
            return f"Error, el numero divisor no es un numero entre 0 y 10"
    else:
        return f"Error, digite dos numero enteros positivos"
#-----------------------------------------------------------------------------------------------

def validar(matriz):
    if(isinstance(matriz,list))and matriz!=[]:
        if(validar_aux(matriz)):
            if largo_aux(matriz):
                return True
            else:
                return False
        else:
            return "Error."
    else:
        return "Error."

def validar_aux(matriz):
    while matriz!=[]:
        if(isinstance(matriz[0],list)):
            if(entero_aux(matriz[0])):
                matriz=matriz[1:]
            else:
                return False
        else:
            return False
    return True

def entero_aux(vector):
    while vector!=[]:
        if(isinstance(vector[0],int)):
            vector=vector[1:]
        else:
            return False
    return True

def largo_aux(matriz):
    comprobar=largoVector(matriz[0])
    while matriz !=[]:
        if(largoVector(matriz[0])==comprobar):   
            matriz=matriz[1:]
        else:
            return False
            
    return True
def largoVector(vector):
    cont=0
    while vector!=[]:
        vector=vector[1:]
        cont+=1
    return cont
