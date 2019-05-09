


#sums all numbers in array except if its 13 and the number after 13


#while loop was better for this as incremnting a for loop in python is weirder than c++
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