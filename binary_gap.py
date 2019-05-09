def solution(N):
    # write your code in Python 3.6
    N = format(N, "b")
    N = list(N)
    count2 = 0
    count  = 0
    print(N)
    for i,j in enumerate(N):
        if int(j) == 0 and int( N[i-1] ) == 1 and i != len(N) -1:
            count = 0
            for x in range(i, len(N)):
                if int(N[x]) == 1:
                    if (count2 < count):
                        count2 = count
                    break
                elif( x == len(N) -1 ):
                    break;
                elif int(N[x]) == 0:
                    count = count + 1

                elif(count2 < count):
                    count2 = count
                else:
                    continue

    return count2







print(solution(234))