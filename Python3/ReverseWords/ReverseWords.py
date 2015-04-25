
with open('input.txt') as fp:
    for line in fp:
        printStr = str()
        for item in line.split()[::-1]:
            printStr = printStr + item + " "
        print(printStr.strip())
