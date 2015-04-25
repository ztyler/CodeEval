with open('input.txt') as fp:
    for line in fp:
        lst = line.split(',')
        count  = 0
        num = 0
        while num < int(lst[0]):
            num = int(lst[1]) * count
            count = count + 1
        print(num)
            
