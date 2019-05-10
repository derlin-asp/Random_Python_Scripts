
def solution(n): #wierdness on comments          len/2 -1 ???
    d = [0] * 30 # d = 30 zeros
    l = 0
    while (n > 0):
        d[l] = n % 2 #makes it a one not 477   using remainders to get down to a one?
        n //= 2
        l += 1
        print(d)
    for p in range(1, 1 + l): #so first loop gets binary? 2nd gets period?
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1
x = 5
x //= 2
print( x)

#print(solution(955))
