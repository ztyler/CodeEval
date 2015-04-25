
with open('input.txt') as test:
    for line in test:
        lineSplit = line.split(';')
        lSplit0 = lineSplit[0].split()
        lSplit1 = lineSplit[1].split()
        lineDict = dict(zip(lSplit1, lSplit0))
        print(lineDict.get('5'))
        '''
        for item in range(len(lSplit1)):
            print(lineDict.get(item))
        ''' 
