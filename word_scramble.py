
import enchant
from itertools import combinations
from itertools import permutations
'''
Takes in a string as input and returns all valid words possible to make with all characters of said string
dictionary used is Enchants Module English Us 
'''

x = "RCONVET"
perms = [''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]
#perms = [''.join(p) for p in combinations('as')]

perms3 = []
for word in perms:
	perms2 = [''.join(p) for p in permutations(word)]
	perms3.append(perms2)


d = enchant.Dict("en_US")
g = enchant.Dict("en_GB")
answers = []
for word in perms3:
	for word2 in word:
		if d.check(word2):# or g.check(word2):
			answers.append(word2)
#print(d.check("ohm"))
#print(perms3)
print (answers)
print (len(answers	))