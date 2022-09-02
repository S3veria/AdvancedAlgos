from asyncio.windows_events import NULL

#actividades es el conjunto C

def select(c):
    """
    Esta función se encarga de seleccionar una actividad
    El criterio de selección es LA ACTIVIDAD CON MENOR DURACIÓN
    """
    #Iniciamos las variables temporales
    minAct=None #Representa el indice de la actividad a seleccionar
    minDur=float('inf') #Representa la duracion de la actividad seleccionada

    #Iteramos a traves de todas las actividades
    for a in range(len(c)):
        #Si la actividad en la que estamos ya fue seleccionada (cuando es None), entonces nos vamos a la siguitente interacion
        if (c[a] is None): 
            continue
        else:
            #Calculamos la duración de la actividad
            currDuration=c[a][1]-c[a][0]
            #Comparamos la duracion actual con la minima
            if currDuration<minDur:
                #Si la duracion actual es menor, entonces seleccionamos esa actividad (temporalmente)
                minDur=currDuration
                minAct=a
    #Regresamos la actividad de menor duración
    return minAct


def feasable(arr,newAct):
    #newAct es tupla
    #arr es solucion
    #Checar si con la nuevaAct hay traslapacion
    #Return a boolean
    """
    Esta función revisa si una actividad dada se puede insertar en nuestra lista de actividades
    Revisa si la actividad nueva se traslapa con alguna de las otras actividades de nuestra lista de actividades
    Regresa un valor booleano
    """
    #Si la actividad nueva no es una actividad, entonces no hay traslape (regresamos True)
    if not newAct:
        return True
    
    #Iteramos a traves de nuestro arreglo de actividades
    for act in arr:
        if act is None:
            continue
        actInitial=act[0]
        actFinal=act[1]
        newActInitial=newAct[0]
        newActFinal=newAct[1]

        #Si se traslapan, entonces regresamos False
        if actInitial<newActInitial and (actFinal>newActInitial):
            return False

        elif actInitial>=newActInitial and (newActFinal>actInitial):
            return False
    #Si no se traslapan, regresamos True
    return True

def greedy(actividades):
    """
    Esta es nuestra función principal para el algoritmo;
    esta itera a través de nuestro arreglo de actividades y selecciona (vorazmente) el mayor numero de actividades que puede
    
    El único parametro de entrada es un arreglo de tuplas (representando actividades),
    en donde el primer índice es la hora de inicio y el segundo es la hora de fin de esa actividad
    """
    solucion=[] #Este es nuestro arreglo de solucion (las actividades que seleccionamos)
    nones=0 #Este es un counter de las actividades que ya seleccionamos o descartamos

    #Iteramos a traves de nuestro arreglo de actividades con un while
    while actividades:
        #Seleccionamos una actividad
        sIndex=select(actividades)
        selected=actividades[sIndex]
        #Cambiamos esa actividad a None(porque la vamos a tomar o descartar)
        actividades[sIndex]=None
        #Incrimentamos nuestro contador
        nones+=1
        #Si seleccionamos una actividad valida y esta cabe dentro de nuestro arreglo de solucion
        if selected and feasable(solucion,selected):
            #Entonces la metemos al arreglo
            solucion.append(selected)
        #Revisamos si nuestro contador es igual a la longitud de nuestro arreglo de actividades
        #En este caso significa que ya revisamos todas las actividades en el arreglo
        if nones==len(actividades):
            #Entocnes nos salimos del while loop
            break
    #Regresamos el arreglo de solucion
    return solucion
        

acts=[(0,6),(1,4),(2,14),(3,5),(4,5),(5,7),(5,9),(6,10),(8,11),(8,12),(12,16)] #Este es el ejemplo en clase de las actividades
print(greedy(acts)) #Imprimimos el resultado del algoritmo
