#FizzBuzz
with open('input.txt') as fp:
    for line in fp:
        #Make line into list
        cleanLine = line.split()
        numList = [ num for num in range(1, int(cleanLine[2]) + 1) ]

        printStr = str()
        for item in numList:
            index = numList.index(item)

            #test devisibility    
            if item % int(cleanLine[0]) == 0:
                numList[index] = "F"
                if item % int(cleanLine[1]) == 0:
                    numList[index] = numList[index] + "B"
            elif item % int(cleanLine[1]) == 0:
                numList[index] = "B"

            printStr = printStr + str(numList[index]) + " "
        print printStr
