
import re
import pprint

total=8
monedas=[0,2,3,7]
matriz=[[None for i in range(total+1)] for j in range(len(monedas))]
pprint.pprint(matriz)
for i in range(len(matriz[0])):
    if i==0:
        matriz[0][i]=0
    else:
        matriz[0][0]=float('inf')

for j in range(len(matriz)):
    matriz[j][0]=0



def cambio(deno,total):
    if (matriz[deno][total]!=None):
        return matriz[deno][total]
    if total==0:
        matriz[deno][total]=0
        return 0
    elif deno==0 and total!=0:
        matriz[deno][total]=float('inf')
        return float('inf')
    if monedas[deno]>total:
        res= cambio(deno-1,total)
        matriz[deno][total]=res
        return res
    else:
        res= min(cambio(deno-1,total), cambio(deno,total-monedas[deno])+1)
        matriz[deno][total]=res
        return res      

"""
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

monedasTotales=cambio(3,total)
pprint.pprint(matriz)

def cualesMonedas(m, i, j):
    res=[]
    while m[i][j] not in (float('inf'), 0):
        if i>0 and m[i][j]==m[i-1][j]:
            i-=1
        else:
            res.append(monedas[i])
            j-=monedas[i]
    return res

print(f'Numero de monedas: {monedasTotales}')
print(f'Monedas: {cualesMonedas(matriz,len(monedas)-1,total)}')

        
        

