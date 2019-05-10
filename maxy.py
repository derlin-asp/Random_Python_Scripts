def solution(A):

    value = max(A)

    for i, e in reversed(list(enumerate(A))):
        if e == value:
            return i



print(solution( [4,6,2,2,6,6,4]   ))