'''
Groups anagrams by eachother

'''


Input = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']

def group_anagrams(items):
    # TODO: Implement me
    if items is None:
        raise TypeError('Cannot be none')
    if not items:
        return items
    listy = []

    #sorting copy og items
    for x in items:
        y = sorted(x)
        listy.append(  ( x,''.join(y) ) ) #making it a tuple of ( new , original )

    listy = sorted(listy, key=lambda tup: tup[1])  #lookup sorted method    #sorting it by original version
    print(listy)

    res_list = [ x[0] for x in listy ]
    return  res_list


group_anagrams(Input)
