from neighborjoin import *
from readMatrix import *
import argparse
from Bio import Phylo
import pylab
from io import StringIO
from UPGMA import *


def main():

    parser = argparse.ArgumentParser(description="Model a tree relationship of organisms based on a distance matrix")
    parser.add_argument("-i", help="Input file", required=True)
    parser.add_argument("-f", help= "Type of function: n for neighbor joining and u for UPGMA", required=True)

    args = parser.parse_args()

    inFile = args.i
    func = args.f
    func.lower()

    distMat = readMatrix(inFile)


    if func == "n":
        #run neighbor joining
        distArr = neighborjoin(distMat)
        strVer = distArrToVisualStyle(distArr)



    elif func == "u":
        matrix=distMat
        copyMatrix=matrix
        clusterSize=1
        halfBranch=[]
        nodes=[]
        clusters=[]
        idxNodes=[]
        treeArr=[]
        lineage=[0]
        while len(matrix)>2:
            shortest=findShortest(matrix,clusterSize,halfBranch,clusters,treeArr)
            updateRes=updateDist(shortest,matrix,copyMatrix,nodes,idxNodes,clusters)   
        for v in range(1,len(halfBranch)):
            lineage.append(abs(halfBranch[v]-halfBranch[v-1]))
        treeStr="(("+treeArr[0]+":"+str(halfBranch[0])+","+" "+treeArr[1]+":"+str(halfBranch[0])+")"+":"+str(lineage[0])
        for b in range(3,len(treeArr),2):
            treeStr+="(("+treeArr[b]+":"+str(halfBranch[int(b/2)])+")"+":"+str(lineage[int(b/2)])+")"
        treeStr+=")"
        
        strVer=treeStr
    else:
        print("Error: invalid commandline arguments")
        
        
    handle = StringIO(strVer)
    tree = Phylo.read(handle, 'newick')
    Phylo.draw(tree)


main()
