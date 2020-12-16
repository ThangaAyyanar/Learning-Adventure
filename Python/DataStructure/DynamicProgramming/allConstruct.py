
def allConstruct(target,wordbank):
    if target == "":
        return [[]] # Base case 

    totalArray = []

    for word in wordbank:
        if target.startswith(word):
            split = target[len(word):]
            numberOfWays = allConstruct(split,wordbank)
            if len(numberOfWays) > 0:
                for ways in numberOfWays:
                    totalArray.append([word] + ways)

    return totalArray

def allConstructTabulation(target,wordbank):
    table = [None] * (len(target)+1)
    table[0] = [[]]

    for i in range(len(target)+1):

        if table[i] != None:
            for word in wordbank:
                split = target[i:i+len(word)]
                if word == split and i+len(word) < len(target)+1:
                    combinations = []
                    for ways in table[i]:
                        combinations.append([ word ]+ways)
                    if table[i+len(word)]:
                        for ways in combinations:
                            table[i+len(word)].append(ways)
                    else:
                        table[i+len(word)] = combinations
    # print(table)
    return table[len(target)]

print(allConstruct("purple",["purp","p","ur","le","purpl"]))
print(allConstructTabulation("abcdef",["ab","abc","cd","def","abcd","ef","c"]))
# print(allConstructTabulation("purple",["purp","le"]))

