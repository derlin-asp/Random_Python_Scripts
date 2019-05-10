# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    for x in A:
        if A.count(x) % 2 != 0:
            return x

    pass



print(solution ( [1,2,3,4,5,1,2,3,5] ))