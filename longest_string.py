n = raw_input("dasdad")


def finder( S ):
    char = []
    count = 0
    stack = []
    temps = ""
    for c in S:
        if ( S.count(c) >= count ):  #this will always grab first letter
            if( c not in char):
                count = S.count(c)
                char.append(c)
    count2 = 0
    #for x in char:
    #    print(  re.compile('x{count}').findall(S)   )
    for x in range(len(char)):
        for index,value in enumerate(S):
            if( char[x] == value ):
                temps += char[x]
                count2 += 1
                #print char[x]
            if(char[x] != value ):
                stack.append(temps)
                temps = ""
                count2=0
    lenList = []
    for x in stack:
        lenList.append(len(x))
    length = max(lenList)
    print("Longest string is: {} at {} characters.".format(stack[lenList.index(length)] , length))

finder(n)
