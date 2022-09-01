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

                #Checking for lateral collision
                if queenCountRow>1:
                    return False
            
                #Explore bottom right diagonal
                currRow=i+1
                currColumn=j+1

                while currRow<=floor and currColumn<=right:
                    if inMat[currRow][currColumn]!=0:
                        #print("bottom right collision")
                        return False
                    currRow+=1
                    currColumn+=1
                
                #Explore bottom left diagonal

                currRow=i+1
                currColumn=j-1

                while currRow<=floor and currColumn>=left:
                    if inMat[currRow][currColumn]!=0:
                        #print("bottom left collision")
                        return False
                    currRow+=1
                    currColumn-=1
                
                #Explore top right diagonal

                currRow=i-1
                currColumn=j+1

                while currRow>=ceiling and currColumn<=right:
                    if inMat[currRow][currColumn]!=0:
                        #print("top right collision")
                        return False
                    currRow-=1
                    currColumn+=1
                
                #Explore top left diagonal

                currRow=i-1
                currColumn=j-1

                while currRow>=ceiling and currColumn>=left:
                    if inMat[currRow][currColumn]!=0:
                        #print("top left collision")
                        return False
                    currRow-=1
                    currColumn-=1


            #Checking for vertical collision
            if inMat[j][i]!=0:
                queenCountColumn+=1
                if queenCountColumn>1:
                    return False

    return True


def isSolution(inMat, lastInsertedQueen):
    if lastInsertedQueen==len(inMat) and isValid(inMat):
        return True
    return False


def exploreBoards(inMat,currQueen):
    #print("Aqui va algo raro")
    sols=[]
    if currQueen>len(inMat):
        return sols
    for i in range(len(inMat[currQueen-1])):
        trialMat=copy.deepcopy(inMat)
        trialMat[currQueen-1][i]=currQueen
        if isSolution(trialMat, currQueen):
            #print(trialMat)
            sols.append(trialMat)
            return sols

        if isValid(trialMat):
            sol=exploreBoards(trialMat,currQueen+1)
            #print(sol)
            if sol:
                for i in sol:
                    newSol=copy.deepcopy(i)
                    #print(newSol)
                    sols.append(newSol)

    return sols



def solveNQueens(n):
    mat=[]
    for i in range(n):
        mat.append([0 for i in range(n)])
    return exploreBoards(mat,1)


        
def printMatrix(mat):
    for i in mat:
        print(i)
    print("-------------------------------")


#tMatrix=[[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#print(isValid(tMatrix))
#print(solveNQueens(4))
nQueens4=solveNQueens(4)
for solution in nQueens4:
    printMatrix(solution)