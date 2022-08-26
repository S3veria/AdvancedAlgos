from numpy import matrix


print("Si le sabemos a git")
print("Lo se, somos god")
import pprint

def isValid(inMat):
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
                if queenCountRow>1:
                    return False
            
                #Explore bottom right diagonal
                currRow=i+1
                currColumn=j+1

                while currRow<=floor and currColumn<=right:
                    if inMat[currRow][currColumn]!=0:
                        print("bottom right collision")
                        return False
                    currRow+=1
                    currColumn+=1
                
                #Explore bottom left diagonal

                currRow=i+1
                currColumn=j-1

                while currRow<=floor and currColumn>=left:
                    if inMat[currRow][currColumn]!=0:
                        print("bottom left collision")
                        return False
                    currRow+=1
                    currColumn-=1
                
                #Explore top right diagonal

                currRow=i-1
                currColumn=j+1

                while currRow>=ceiling and currColumn<=right:
                    if inMat[currRow][currColumn]!=0:
                        print("top right collision")
                        return False
                    currRow-=1
                    currColumn+=1
                
                #Explore top left diagonal

                currRow=i-1
                currColumn=j-1

                while currRow>=ceiling and currColumn>=left:
                    if inMat[currRow][currColumn]!=0:
                        print("top left collision")
                        return False
                    currRow-=1
                    currColumn-=1


            if inMat[j][i]!=0:
                queenCountColumn+=1
                if queenCountColumn>1:
                    return False

    return True

def solveNQueens(n):
    mat=[]
    for i in range(n):
        mat.append([0 for i in range(n)])
    pprint.pprint(mat)


        
                


tMatrix=[[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(isValid(tMatrix))
solveNQueens(4)