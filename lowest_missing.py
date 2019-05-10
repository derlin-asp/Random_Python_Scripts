


def solution(A):
    # write your code in Python 3.6
    #filter(lambda x: x > 0, A)

    B = [x for x in A if x > 0]

    B.sort()
    #print(B)

    #print(len(B))
    if not b:
        return 1
    for i in range(1,len(B)):
        if i not in B:
            return i
    return B[-1] + 1

print(solution( [1,2,3] ))