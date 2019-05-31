#funtion to read an input txt file and create the list of lists version of the distance matrix


def readMatrix(inFile):
    readFile = open(inFile, "r")
    distMat = [[None]]

    tempLine = readFile.readline()

    while (tempLine == "\n" or tempLine[0] == "#"):
        tempLine = readFile.readline()



    #reached the actual matrix

    tempLineArr = tempLine.split()
    for val in range(len(tempLineArr)):
        distMat[0].append(tempLineArr[val])


    #for all rows after index 0
    for i in range(1, len(distMat[0])):
        tempLine = readFile.readline()
        tempLineArr = tempLine.split()
        distMat.append([])

        for val in range(len(tempLineArr)):
            if val != 0:
                distMat[i].append(float(tempLineArr[val]))

            else:
                distMat[i].append(tempLineArr[val])


    readFile.close()

    return distMat