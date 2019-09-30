'''
Sums an array - minus the elements that are equal 13 and the subsequent element
'''

#orignial
def sum13(array):

    sum = 0
    x = 0
    while x != len(array):
        if array[x] != 13:
            sum = sum + array[x]
        if array[x] == 13:
            x = x + 1
        x = x + 1
        #print(x)
    return sum



print (sum13([1,2,1,13,5,11]))

