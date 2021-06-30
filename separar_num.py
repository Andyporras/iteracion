def separar_num(num):
    if(isinstance(num,int)):
        if(num>0):
            par=[]
            impar=[]
            while num!=0:
                if(num%10)%2==0:
                    par+=[num%10]
                    num=num//10
                else:
                    impar+=[num%10]
                    num=num//10
            else:
                if(par!=[]):
                    result2=[]
                    while par!=[]:
                        result2+=[par[-1]]
                        par=par[:-1]
                    else:
                        if(impar!=[]):
                            result3=[]
                            while impar!=[]:
                                result3+=[impar[-1]]
                                impar=impar[:-1]
                            return result3+result2
                        else:
                            return result2
                else:
                    result3=[]
                    while impar!=[]:
                        result3+=[impar[-1]]
                        impar=impar[:-1]
                    return result3+result2
                    
            
                            
                
           
