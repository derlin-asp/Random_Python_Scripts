
import enchant
from itertools import combinations
from itertools import permutations
'''

def primer(string):
	list_of_new_strings = []
	list_of_new_strings.append(string)
	for c in range( len(string) ):
		if c == 0:
			continue
		temp = (string[c] + string[c-1::-1 ] + string[c+1::1] )
		list_of_new_strings.append(temp)
	return list_of_new_strings
	
'''


x = "FARNGLI"
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
print answers
print len(answers	)