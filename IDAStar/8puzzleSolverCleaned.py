from copy import deepcopy


# puzzle = [[7,2,4],
#           [5,0,6],
#           [8,3,1]]

puzzle = [[1,2,3],
          [4,5,0],
          [7,8,6]]


resDict={
    0:(2,2),
    1:(0,0),
    2:(0,1),
    3:(0,2),
    4:(1,0),
    5:(1,1),
    6:(1,2),
    7:(2,0),
    8:(2,1)
}

def printPuzzle(p):
    for line in p:
        for num in line:
            if num == 0:
                print(" ", end=" ")
            else:
                print(num, end=" ")
        print()

def readPuzzle(fileName: str):
    file = open(fileName, 'r+')
    lines = file.readlines()
    m = []
    for line in lines:
        intLine = []
        for c in line[:-1]:
            intLine.append(int(c))
        m.append(intLine)
    return m

def calcH(mat):
    h=0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            at=mat[i][j]
            iDif=abs(i-resDict[at][0])
            jDif=abs(j-resDict[at][1])
            h+=(iDif+jDif)
    return h

def generateStates(mat):
    myI=0
    myJ=0
    encontrado=False
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==0:
                myI=i
                myJ=j
                encontrado=True
                break
        if encontrado:
            break
    #Ya encontramos el 0
    
    #Determinar posibles numeros a mover a la posición del 0
    #Este proceso resulta en un arreglo de estados posibles del puzzle
    stateArr=[]
    if myI<len(mat)-1:
        #down
        newMat=deepcopy(mat)
        #Hacemos swap
        newMat[myI][myJ]=newMat[myI+1][myJ]
        newMat[myI+1][myJ]=0
        stateArr.append((newMat, calcH(newMat)))
    if myI>0:
        #up
        newMat=deepcopy(mat)
        #Hacemos swap
        newMat[myI][myJ]=newMat[myI-1][myJ]
        newMat[myI-1][myJ]=0
        stateArr.append((newMat, calcH(newMat)))
    if myJ<len(mat[0])-1:
        #left
        newMat=deepcopy(mat)
        #Hacemos swap
        newMat[myI][myJ]=newMat[myI][myJ+1]
        newMat[myI][myJ+1]=0
        stateArr.append((newMat, calcH(newMat)))
    if myJ>0:
        #right
        newMat=deepcopy(mat)
        #Hacemos swap
        newMat[myI][myJ]=newMat[myI][myJ-1]
        newMat[myI][myJ-1]=0
        stateArr.append((newMat, calcH(newMat)))
    return stateArr

class treeNode():
  def __init__(self, fatherState, myState, hVal, gVal):
    self.father=fatherState
    self.state=myState
    self.h=hVal
    self.g=gVal
    self.children=[] #Vamos a guardar mas treeNodes
  def getValues(self):
    return {"h":self.h, "g": self.g}
  def getChildren(self):
    return self.children
  def getState(self):
    return self.state
  def addChildren(self, newChildren):
    for c in newChildren:
      self.children.append(c)
  def getChildren(self):
    return self.children
  def getParent(self):
    return self.father
  def print(self):
    print('--------------------------')
    print(f"h: {self.h}, g: {self.g}")
    printPuzzle(self.state)


firstNode=treeNode(None,puzzle,calcH(puzzle),0)

stateQueue=[(firstNode, [firstNode.getState()])]
stateStack=[]
def iterativeMakeChildren(node, maxDepth=float('inf'), visited=[]):
  
  visited.append(node.getState())
  currentValues=node.getValues()
  if currentValues['h']==0:

    return (node,node) #Este es nuestro camino optimo
  if currentValues['g']>maxDepth:
    return (node,None)
                   
  newStates=generateStates(node.getState())
  newNodes=[]
  minH=float('inf')
  for i in newStates:      
    newNode=treeNode(node, i[0], i[1], node.getValues()["g"]+1)
    newNodes.append(newNode)
    #visited.append(i)
    if i[1]<minH and i[0] not in visited:
      minH=i[1]
  optimalNode=None
  for n in newNodes:
    
    #bucle de empates
    if n.getValues()['h']==minH : 
      stateQueue.append((n, visited))
    elif n.getState() not in visited:
      stateStack.append((n, visited))

  node.addChildren(newNodes)
  return (node,optimalNode, visited)

def findSolution():
    maxD=float('inf')
    optimalNode=None
    while stateQueue or stateStack:
        currentN=()
        if stateQueue:
            currentN=stateQueue.pop(0)
        else:
            currentN=stateStack.pop(-1)
        functionCall=iterativeMakeChildren(currentN[0], visited=currentN[1], maxDepth=maxD)
        resOptimalNode=functionCall[1]
        if resOptimalNode and resOptimalNode.getValues()['g']<maxD:
            optimalNode=resOptimalNode
            optimalNode.print()
            maxD = optimalNode.getValues()['g']
            print(maxD)

    optimalNode.print()
    #Encontrar el path
    path=[]
    node=optimalNode
    while node:
        path.append(node.getState())
        node=node.getParent()
    #Imprimir el path
    path=path[::-1]
    for mat in path:
        print("---------step---------")
        for i in mat:
            print(i)

findSolution()
