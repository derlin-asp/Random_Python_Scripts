'''
Finds lowest missing positive number:

N time complexity

1 Space Complexity

{2, 3, 7, 6, 8, -1, -10, 15} = 1
'''


def solution(elements):
    elements.sort()
    # Time : nlogn
    # space : Constant
    print(elements)


    count = 0;
    for i,num in enumerate(elements):
        if num >= 0 and num == count:
            count += 1
        elif num >= 0 and num != count:
            return count
        else:
            print("Negative Number")





print(solution( [0,1,2,6,9] ))