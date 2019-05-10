
#takes in an in and returns the "Ziped version" 130 = 103  etc

#123456 = 162534   etc
def solution(A):
    # write your code in Python 3.6
    A = list(str(A))
    # copy array and reverse it
    B = A[::-1]

    C = []
    x = 0
    while ( len(C) < len(A) ):
        C.append(A[x])
        if len(C) < len(A):
            C.append(B[x])
        x = x + 1
    s = [str(i) for i in C]
    C = int("".join(s))
    return C

print(solution(130))