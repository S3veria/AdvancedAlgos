#Max actividades
from asyncio.windows_events import NULL

#actividades es el conjunto C

def select(c):
    #Buscamos el menor
    #Podriamos hacer un sort
    #return an index
    minAct=None
    minDur=float('inf')
    for a in range(len(c)):
        if (c[a] is None): 
            continue
        else:
            currDuration=c[a][1]-c[a][0]

            if currDuration<minDur:
                minDur=currDuration
                minAct=a
    return minAct


def feasable(arr,newAct):
    #newAct es tupla
    #arr es solucion
    #Checar si con la nuevaAct hay traslapacion
    #Return a boolean
    if not newAct:
        return True
    for act in arr:
        if act is None:
            continue
        actInitial=act[0]
        actFinal=act[1]
        newActInitial=newAct[0]
        newActFinal=newAct[1]

        if actInitial<newActInitial and (actFinal>newActInitial):
            return False

        elif actInitial>=newActInitial and (newActFinal>actInitial):
            return False

    return True

def greedy(actividades):
    solucion=[]
    nones=0

    #Aqui checar si cabe algo mas
    while actividades:
        sIndex=select(actividades)
        selected=actividades[sIndex]
        actividades[sIndex]=None

        nones+=1
        if selected and feasable(solucion,selected):
            solucion.append(selected)
        if nones==len(actividades):
            break
    return solucion
        

acts=[(0,6),(1,4),(2,14),(3,5),(4,5),(5,7),(5,9),(6,10),(8,11),(8,12),(12,16)]
print(greedy(acts))
