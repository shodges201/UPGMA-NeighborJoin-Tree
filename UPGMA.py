
import sys
import math


def findShortest(matrix,clusterSize,halfBranch,clusters,treeArr):
    print(matrix)
    clusterRow=0
    newCluster=""
    newClusterCol=""
    newClusterRow=""
    result=[]
    clusterCol=0
    for u in range(1, len(matrix)):
        acc=0
        shortestDist = float("inf")
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix)):
                if matrix[i][j] < shortestDist and matrix[i][j] != 0:
                    shortestDist = matrix[i][j]
                    clusterRow = i
                    clusterCol = j
        newClusterCol = str(matrix[0][clusterCol])
        newClusterRow = str(matrix[clusterRow][0])
        newCluster = newClusterRow + newClusterCol
        clusters.append(newCluster)
    treeArr.append(newClusterRow)
    treeArr.append(newClusterCol)
    halfBranch.append(shortestDist / 2)
    clusterSize=len(newCluster)
    result.append(newCluster)
    result.append(clusterSize)
    result.append(newClusterRow)
    result.append(newClusterCol)
    result.append(clusters)
    result.append(halfBranch)

    return result

def updateDist(shortest,matrix,copyMatrix,nodes,idxNodes,clusters):
    newCluster=shortest[0]
    clusterSize=shortest[1]
    newClusterRow=shortest[2]
    newClusterCol=shortest[3]
    used=[]
    if newClusterCol not in matrix[0]:
        idxCol=copyMatrix[0].index(str(newClusterCol))
    else:
        idxCol=matrix[0].index(str(newClusterCol))
    if newClusterRow not in matrix[0]:
        idxRow = copyMatrix[0].index(str(newClusterRow))
    else:
        idxRow=matrix[0].index(str(newClusterRow))

    for t in range(1,len(matrix)-1):
        if matrix[t][idxCol]==0:
            t+=1
            if t>len(matrix):
                break
        elif matrix[idxRow][t]==0:
            t+=1
            if t>len(matrix):
                break

        if newClusterCol not in clusters:
            nodes.append(newClusterCol)
        if newClusterRow not in clusters:
            nodes.append(newClusterRow)
        for n in range(0,len(nodes)):
            if nodes[n] in copyMatrix[0]:
                temp=copyMatrix[0].index(nodes[n])
                idxNodes.append(temp)

        acc=0
        for x in range(0,len(copyMatrix)):
            if t==newClusterCol or t==newClusterRow:
                continue
            else:
                if x in idxNodes:
                    acc+=copyMatrix[t][x]

        matrix[idxRow][t]=acc/clusterSize
        matrix[t][idxRow]=acc/clusterSize
    matrix[0][idxRow]=newCluster
    matrix[idxRow][0]=newCluster
    del matrix[matrix[0].index(str(newClusterCol))]
    for r in range(0,len(matrix)):
        del matrix[r][idxCol]
    print(matrix)
    results=[matrix,idxNodes,nodes]
    return results

#
# def main():
#     infile=sys.argv[1]
#     matrix=readMatrix(infile)
#     copyMatrix=matrix
#     clusterSize=1
#     halfBranch=[]
#     nodes=[]
#     clusters=[]
#     idxNodes=[]
#     treeArr=[]
#     lineage=[0]
#     while len(matrix)>2:
#         shortest=findShortest(matrix,clusterSize,halfBranch,clusters,treeArr)
#         updateRes=updateDist(shortest,matrix,copyMatrix,nodes,idxNodes,clusters)
#
#     print(halfBranch)
#     print(treeArr)
#     for v in range(1,len(halfBranch)):
#         lineage.append(abs(halfBranch[v]-halfBranch[v-1]))
#     print(lineage)
#     treeStr="(("+treeArr[0]+":"+str(halfBranch[0])+","+" "+treeArr[1]+":"+str(halfBranch[0])+")"+":"+str(lineage[0])
#     for b in range(3,len(treeArr),2):
#         treeStr+="(("+treeArr[b]+":"+str(halfBranch[int(b/2)])+")"+":"+str(lineage[int(b/2)])+")"
#     treeStr+=")"
#     print(treeStr)
#     handle = StringIO(treeStr)
#     tree = Phylo.read(handle, 'newick')
#     Phylo.draw(tree)
#
#
