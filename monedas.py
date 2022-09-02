import re
import pprint

#Definir el total de dinero a cambiar
total=8
#Definir las monedas que tenemos dispoibles (El 0 tiene que estar incluido)
monedas=[0,2,3,7]
#Hacemos una matriz vacia (Llena de valores None)
matriz=[[None for i in range(total+1)] for j in range(len(monedas))]
pprint.pprint(matriz)

#Llenamos la primera fila con 0s y el primero con infinito
for i in range(len(matriz[0])):
    if i==0:
        matriz[0][i]=0
    else:
        matriz[0][0]=float('inf')

#Llenamos la primer columna de 0s
for j in range(len(matriz)):
    matriz[j][0]=0



def cambio(deno,total):
    """
    Esta es la funcion principal, regresa el numero minimo de de monedas que se pueden dar de cambio
    """
    #Si en el valor en el que estamos esta marcado como None, entonces regresamos None
    if (matriz[deno][total]!=None):
        return matriz[deno][total]
    #Si el total de monedas es 0, entonces metemos el valor en la matriz y lo regresamos
    if total==0:
        matriz[deno][total]=0
        return 0
    #Si la denominacion es 0 y el total no es 0, entonce el cambio en moendas es impossible
    elif deno==0 and total!=0:
        matriz[deno][total]=float('inf')
        return float('inf')
    #Si la denominacion es mayor al total, entonces tenemos que bajar la denominacion. Metemos esta info en la matriz.
    if monedas[deno]>total:
        res= cambio(deno-1,total)
        matriz[deno][total]=res
        return res
    #De otra forma, si podemos utilizar la denominacion en el total
    else:
        #El resultado sera el minimo entre utilizar esa denominacion de moneda o utilizar una denominacion menor
        res= min(cambio(deno-1,total), cambio(deno,total-monedas[deno])+1)
        #Aqui metemos el resultado en la matriz
        matriz[deno][total]=res
        return res      

"""
#Esta es la funcion que resulve el problema sin dynamic programming
def cambioSinDP(deno, total):
    if total==0:
        return 0
    elif deno==0 and total!=0:
        return float('inf')
    if(monedas[deno]>total):
        return cambioSinDP(deno-1,total)
    else:
        return min(cambioSinDP(deno-1,total),cambioSinDP(deno,total-monedas[deno])+1)
"""

monedasTotales=cambio(3,total) #Aqui obtenemos la solucion al problema
#pprint.pprint(matriz) 

def cualesMonedas(m, i, j):
    """
    Esta funcion nos ayuda a encontrar las monedas que solucionan el problema dada
        la matriz m,
        el numero de denominaciones de monedas
        y el total de dinero a cambiar
    """
    res=[]
    while m[i][j] not in (float('inf'), 0):
        if i>0 and m[i][j]==m[i-1][j]:
            i-=1
        else:
            res.append(monedas[i])
            j-=monedas[i]
    return res

print(f'Numero de monedas: {monedasTotales}') #Imprimimos el numero de monedas
print(f'Monedas: {cualesMonedas(matriz,len(monedas)-1,total)}') #Imprimimos cuales monedas dan solucion al problema

        
        

