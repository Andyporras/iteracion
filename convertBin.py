def convertBin(n):
    if(isinstance(n,int)and n>0):
        return convertBin_aux(n,0,0)
    else:
        return "Error"


def convertBin_aux(n,result,cont):
    if(n==0):
        return result
    else:
        result+=(n%2)*(10**cont)
        return convertBin_aux(n//2,result,cont+1)
#--------------------------------------------
    
def deBinADesimal(n):
    if(isinstance(n,int)and n>=0):
        return deBinADesimal_aux(n,0,0)
    else:
        return "Error"

def deBinADesimal_aux(n,cont,result):
    if(n==0):
        return result
    else:
        result+=((n%10)*(2**cont))
        return deBinADesimal_aux(n//10,cont+1,result)

#...................................................................


def deBinADesimalV2(n):
    if(isinstance(n,int)and n>=0):
        return deBinADesimalV2_aux(n,0,0)
    else:
        return "Error"

def deBinADesimalV2_aux(n,result,cont):
    if(n==0):
        return result
    else:
        print((n%10)*(2**cont))
        return deBinADesimal_aux(n//10,result+((n%10)*(2**cont)),cont+1)

#---------------------------------------------------------------------------

    
def aBase3(n):
    if(isinstance(n,int)and n>0):
        return aBase3_aux(n,0,0)
    else:
        return "Error"


def aBase3_aux(n,result,cont):
    if(n==0):
        return result
    else:
        result+=(n%3)*(10**cont)
        return aBase3_aux(n//3,result,cont+1)


#------------------------------------------------------------------

def deBase3Adecimal(n):
    if(isinstance(n,int)and n>=0):
        return deBase3Adecimal_aux(n,0,0)
    else:
        return "Error"

def deBase3Adecimal_aux(n,cont,result):
    if(n==0):
        return result
    else:
        result+=((n%10)*(3**cont))
        return deBase3Adecimal_aux(n//10,cont+1,result)

#------------------------------------------------------------

    
def hexadecimal(hexa):
    if(isinstance(hexa,str)):
        return hexadecimal_aux(hexa,0,0)
    else:
        return "Error"

def hexadecimal_aux(hexa,result,cont):
    if(hexa==""):
        return result
    elif(hexa[-1]=="f"):
        result+=(15*(16**cont))
        return hexadecimal_aux(hexa[:-1],result,cont+1)
    elif(hexa[-1]=="e"):
        result+=(14*(16**cont))
        return hexadecimal_aux(hexa[:-1],result,cont+1)
    elif(hexa[-1]=="d"):
        result+=(13*(16**cont))
        return hexadecimal_aux(hexa[:-1],result,cont+1)
    elif(hexa[-1]=="c"):
        result+=(12*(16**cont))
        return hexadecimal_aux(hexa[:-1],result,cont+1)
    elif(hexa[-1]=="b"):
        result+=(11*(16**cont))
        return hexadecimal_aux(hexa[:-1],result,cont+1)
    elif(hexa[-1]=="a"):
        result+=(10*(16**cont))
        return hexadecimal_aux(hexa[:-1],result,cont+1)
    else:
        suma=int(hexa[-1])
        result+=(suma*(16**cont))
        return hexadecimal_aux(hexa[:-1],result,cont+1)
#---------------------------------------------------------------

    
def decimalAHexa(n):
    if(isinstance(n,int)and n>0):
        return decimalAHexa_aux(n,"",0)
    else:
        return "Error"


def decimalAHexa_aux(n,result,cont):
    if(n==0):
        return ordenar_aux(result,"")
    else:
        suma=(n%16)
        if(suma==15):
            return decimalAHexa_aux(n//16,result+"f",cont+1)
        elif(suma==14):
            return decimalAHexa_aux(n//16,result+"e",cont+1)
        elif(suma==13):
            return decimalAHexa_aux(n//16,result+"d",cont+1)
        elif(suma==12):
            return decimalAHexa_aux(n//16,result+"c",cont+1)
        elif(suma==11):
            return decimalAHexa_aux(n//16,result+"b",cont+1)
        elif(suma==10):
            return decimalAHexa_aux(n//16,result+"a",cont+1)
        else:
            suma=str(suma)
            return decimalAHexa_aux(n//16,result+suma,cont+1)

def ordenar_aux(hexa,result):
    if(hexa==""):
        return result
    else:
        return ordenar_aux(hexa[:-1],result+hexa[-1])


def disminuirMatriz(matriz):
    if isinstance(matriz,list):
        if validaMatriz(matriz):
            if tamaño(matriz):
                Lista = []
                for Lista2 in matriz:
                    for vector in Lista2:
                        if vector%2 == 1:
                            Lista += [vector]
                        else:
                            continue
                largoLista = largo_lista(Lista,0)
                contador = 0
                contador2 = contador
                while contador <= largoLista:
                    if(largoLista >=(contador*contador)):

                        contador2=contador
                        contador+=1

                    else:
                        contador+=1
                    
                Fila = contador2
                columnaActual = 0
                filaActual = 0
                resultado = []
                suma = []
                while Lista!=[]:
                    if columnaActual == contador2:
                        columnaActual = 0
                        filaActual += 1
                        resultado += [suma]
                        suma=[]
                    elif(filaActual==contador2):
                        Lista=Lista[1:]
                    else:
                        suma += [Lista[0]]
                        columnaActual += 1
                        Lista=Lista[1:]
                return resultado
                    
            
            else:
                return 'Error: existen vectores de diferentes tamaños'
        else:
            return "La matriz debe tener números enteros"
    else:
        return "La matriz debe ser una lista"

def validaMatriz(matriz):
    for vectores in matriz: 
        if isinstance(vectores,list):
            for indices in vectores:
                if isinstance(indices,int):
                    continue
                else:
                    return False
        else:
            return False
    return True


def tamaño(matriz):
    indice1 = matriz[0]
    for indices in matriz:
        if largo_lista(indices,0)== largo_lista(indice1,0):
            continue
        else:
            return False
    else:
        return True

def largo_lista(lista,contador):
    while lista != []:
        contador += 1
        lista = lista[1:]
    return contador

