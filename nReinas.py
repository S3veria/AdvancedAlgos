import pprint
import copy

def isValid(inMat):
    """
    Esta funcion checa si una matriz es valida o no (si hay colisiones de reinas o no)
    Nota: Se deberia de llamar una vez que se inserta una reina nueva para ver si se vale o no
    """
    queenCountRow=0
    queenCountColumn=0

    #Dimensions for the matrix
    ceiling=0
    floor=len(inMat)-1
    left=0
    right=floor

    for i in range(len(inMat)):
        queenCountRow=0
        queenCountColumn=0
        for j in range(len(inMat)):
            if inMat[i][j]!=0:
                queenCountRow+=1

                #Checamos si hay colisiones horizontales
                if queenCountRow>1:
                    return False
            
                #Exploramos la diagonal inferior derecha
                currRow=i+1
                currColumn=j+1

                while currRow<=floor and currColumn<=right:
                    if inMat[currRow][currColumn]!=0:
                        #print("bottom right collision")
                        return False
                    currRow+=1
                    currColumn+=1
                
                #Exploramos la diagonas inferior izquierda
                currRow=i+1
                currColumn=j-1

                while currRow<=floor and currColumn>=left:
                    if inMat[currRow][currColumn]!=0:
                        #print("bottom left collision")
                        return False
                    currRow+=1
                    currColumn-=1
                
                #Exploramos la diagonal superior derecha
                currRow=i-1
                currColumn=j+1

                while currRow>=ceiling and currColumn<=right:
                    if inMat[currRow][currColumn]!=0:
                        #print("top right collision")
                        return False
                    currRow-=1
                    currColumn+=1
                
                #Exploramos la diagonal superior izquierda 
                currRow=i-1
                currColumn=j-1

                while currRow>=ceiling and currColumn>=left:
                    if inMat[currRow][currColumn]!=0:
                        return False
                    currRow-=1
                    currColumn-=1


            #Revisamos si hay una colision vertical
            if inMat[j][i]!=0:
                queenCountColumn+=1
                if queenCountColumn>1:
                    return False

    #Si no hay ninguna colision, entonces regresamos True
    return True


def isSolution(inMat, lastInsertedQueen):
    """
    Esta función checa si un tablero es una solución para el problema de nreinas
    Regresa un valor booleano

    Parametors:
    La ultima reina que se insertó (Lo comparamos con la longitud de la Matriz)
    La matrizen en la que insertamos la úlitma reina
    """
    if lastInsertedQueen==len(inMat) and isValid(inMat):
        return True
    return False


def exploreBoards(inMat,currQueen):
    """
    Esta es la función recursiva en la que estaremos explorando las distintas posibles soliciones del problema
    Se llama esta función con la matriz vacia y con 1 como la llamada inicial del problema (ejecutado por solveNQueens)
    """

    #Tenemos un arreglo de soluciones, que inicialmente esta vacio
    sols=[]

    #Si la reina a insertar es mayor a la longitud de la matriz, no es una reina valida
    #Entonces regresamos el arreglo de soliciones (vacio)
    if currQueen>len(inMat):
        return sols

    #Iteramos a traves de la longid de la matriz (para los posibles posicionamientos de las reinas)
    for i in range(len(inMat[currQueen-1])):
        #Copiamos la matriz de parametro
        trialMat=copy.deepcopy(inMat)
        #Insertamos la nueva reina
        trialMat[currQueen-1][i]=currQueen

        #Checamos si el tablero, con el nuevo posicionamiento, es la solucion al problema
        if isSolution(trialMat, currQueen):
            #Agregamos esa solucion al arreglo de soluciones
            sols.append(trialMat)
            #Regresamos el arreglo de soluciones (unicamente con la solucion que acabamos de encontrar)
            #Hacemos esto porque no va a haber mas de una solucion al posicionar la ultima reina en el tablero
            return sols

        #Si el nuevo tablero no es una solucion, checamos si es un tablero valido
        #Si no es valido el tablero entonces no ejecutamos la recursio
        if isValid(trialMat):
            #Hacemos la recursion (con el tablero actual y la siguiente reina)
            sol=exploreBoards(trialMat,currQueen+1)
            
            #Checamos si la llamada recursiva regreso alguna solucion ([] es lo mismo a False en este caso)
            if sol:
                #Iteramos a travez de las soluciones
                for i in sol:
                    #Copiamos cada solucion a una variable nueva
                    newSol=copy.deepcopy(i)
                    #Insertamos la copia dentro del arreglo de soluciones
                    sols.append(newSol)
                    
    #Regresamos el arreglo de soluciones
    return sols



def solveNQueens(n):
    """
    Esta es la funcion que se manda a llamar cuando queremos solucionar el problema de nReinas para un numero n
    """
    #Primero creamos una matriz nxn llena de 0s
    mat=[]
    for i in range(n):
        mat.append([0 for i in range(n)])
    #Comenzamos la exploracion del tablero vacio con la reina 1
    return exploreBoards(mat,1)


        
def printMatrix(mat):
    """
    Esta solo es una funcion para que imprima una matriz por fila (para visualizar las solcuciones)
    """
    for i in mat:
        print(i)
    print("-------------------------------")



nQueens4=solveNQueens(4)
for solution in nQueens4:
    printMatrix(solution)