def separar(lista):
    if(isinstance(lista,list)):
        if(lista!=[]):
            impar=[]
            par=[]
            for n in lista:
                if(n%2)==0:
                    par+=[n]
                else:
                    impar+=[n]
            return [par]+[impar]
        else:
            return "Error: lista vacia"
    else:
        return "Error: no es una lista. "
        
