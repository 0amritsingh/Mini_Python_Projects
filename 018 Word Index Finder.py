# Word Index/Position Finder (in a particular sentance)

def indexing(word, sentance):
    list = []
    place_holder = 0
    for i in range(sentance.count(word)):
        index = sentance.find(word, place_holder, len(sentance))
        place_holder = index + 1
        list.append(index)
    return list

a = 'hello' # the word(a) to find in the follwing sentance(b)
b = 'hello world, hello mom, hello dad, hello pyhon'
print(indexing(a, b))
 