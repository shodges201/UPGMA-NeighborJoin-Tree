import math


def neighborjoin(distMat):

    distArr = []

    while len(distMat) > 3:

        bestPair = findBestPair(distMat, distArr)
        updateDistToNew(bestPair, distMat)

    #updateDistArr(distMat, distArr, i, j, distIToIJ, distJToIJ):
    updateDistArr(distMat, distArr, 1, 2, distMat[1][2], distMat[1][2])


    return distArr

#avgDist in this refers to the average distance from the point to
#every other point except for itself and the it's partner point
#so it's almost the average distance

def findAvgDist(i, j, distMat):

    tempSumI = 0
    tempSumJ = 0

    for row in range(1, len(distMat)):
        if row != i and row != j:
            tempSumI += distMat[row][i]
            tempSumJ += distMat[row][j]


    avgDistI = tempSumI/(len(distMat) - 3)
    avgDistJ = tempSumJ/ (len(distMat) - 3)

    return (avgDistI, avgDistJ)


def findBestPair(distMat, distArr):

    bestPairVal = math.inf


    colMax = 1
    #for every pair of vertices
    for row in range(2, len(distMat)):
        for col in range(1, colMax + 1):

            avgDistTup = findAvgDist(row, col, distMat)

            tempBestPairVal = distMat[row][col] - avgDistTup[0] - avgDistTup[1]
            if tempBestPairVal < bestPairVal:
                bestPairVal = tempBestPairVal
                i = row
                j = col
                ui = avgDistTup[0]
                uj = avgDistTup[1]



        colMax += 1


    distIToIJ = .5*(distMat[i][j] + ui - uj)
    distJToIJ = .5*(distMat[i][j] + uj - ui)

    updateDistArr(distMat, distArr, i, j, distIToIJ, distJToIJ)

    return (i, j)

def updateDistToNew(bestPair, distMat):

    i = bestPair[0]
    j = bestPair[1]
    Mij = distMat[i][j]

    #replace i's letter with ij's letter combination
    iLet = distMat[0][i]
    jLet = distMat[0][j]
    newLet = iLet + jLet

    distMat[i][0] = newLet
    distMat[0][i] = newLet

    #go across the row and down the column of i and update distances as though it is ij
    for cluster in range(1, len(distMat)):
        if cluster != i:
            Mik = distMat[i][cluster]
            Mjk = distMat[cluster][j]

            distToK = (Mik + Mjk - Mij)/2

            distMat[i][cluster] = distToK
            distMat[cluster][i] = distToK


    for cluster in range(len(distMat)):
        del distMat[cluster][j]


    del distMat[j]



def updateDistArr(distMat, distArr, i, j, distIToIJ, distJToIJ):


    newName = distMat[i][0] + distMat[0][j]
    iName = distMat[i][0]
    jName = distMat[0][j]

    iCompound = -1
    jCompound = -1

    #need to delete after, not during for loop so I don't go out of range with idx
    delJ = False


    for idx in range(len(distArr)):
        if distArr[idx][0] == iName and jCompound == -1 and iCompound == -1:
            iCompound = idx
            distArr[idx] = [newName, distArr[idx][:], distIToIJ]
        elif distArr[idx][0] == iName and iCompound == -1:
            iCompound = idx
            distArr[idx] = [newName, distArr[idx][:], distIToIJ]

            distArr[idx].append(distArr[jCompound][0])
            distArr[idx].append(distArr[jCompound][1])

            delJ = True
            #del distArr[jCompound]



        if distArr[idx][0] == jName and iCompound == -1 and jCompound == -1:
            jCompound = idx
            distArr[idx] = [distArr[idx][:], distJToIJ]
        elif distArr[idx][0] == jName and jCompound == -1:
            jCompound = idx
            distArr[iCompound].append(distArr[idx][:])
            distArr[iCompound].append(distJToIJ)

            delJ = True
            #del distArr[idx]

    if delJ:
        del distArr[jCompound]


    if iCompound == -1 and jCompound == -1:
        distArr.append([newName, distMat[i][0], distIToIJ, distMat[0][j], distJToIJ])

    elif iCompound == -1:
        distArr[jCompound].insert(0, distIToIJ)
        distArr[jCompound].insert(0, distMat[i][0])
        distArr[jCompound].insert(0, newName)

    elif jCompound == -1:
        distArr[iCompound].append(distMat[0][j])
        distArr[iCompound].append(distJToIJ)


def distArrToVisualStyle(distArr):

    strVer = str(distArr)
    strVer = strVer[2:-2]
    strVer = "(" + strVer + ");"


    i = 1
    tempCh = strVer[i]
    while tempCh != ",":
        i+=1
        tempCh = strVer[i]

    strVer = "(" + strVer[i+2:]



    i=1
    while i < len(strVer) - 2:

        if strVer[i] == "[":
            strVer = strVer[:i] + "(" + strVer[i+1:]
        elif strVer[i] == "]":
            strVer = strVer[:i] + ")" + strVer[i+1:]
        elif strVer[i] == "'":
            strVer = strVer[:i] + strVer[i+1:]
            #because the string has shrunk by 1
            i-=1



        i+=1


    #if there are negative distances set them to zero instead
    negSignIdx = strVer.find("-")

    while negSignIdx != -1:
        idx2 = negSignIdx
        while strVer[idx2] != ",":
            idx2 += 1

        strVer = strVer[:negSignIdx] + "0.0" + strVer[idx2:]

        negSignIdx = strVer.find("-")



    i = 1
    while i < len(strVer) - 2:

        while (ord(strVer[i]) < 48 or ord(strVer[i]) > 57) and i < len(strVer) - 2:

            i += 1

        if i < len(strVer) - 2:
            strVer = strVer[:i-2] + ":" + strVer[i:]

            while i < len(strVer) - 2 and strVer[i] != ",":
                i+= 1



    i = 1
    parenIdx = -1
    while i < len(strVer) - 2:

        while i < len(strVer) - 2 and strVer[i] != "(":
            i+=1

        while i < len(strVer) - 2 and strVer[i] == "(":
            i+=1

        parenIdx = i - 1

        while i < len(strVer) - 2 and strVer[i] != ",":
            i+= 1

        if i < len(strVer) - 2:
            strVer = strVer[:parenIdx + 1] + strVer[i+2:]

            i = parenIdx + 1



    return strVer