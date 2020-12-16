
def countConstruct(target,wordbank):
    if target == "":
        return 1

    totalCount = 0

    for word in wordbank:
        if target.startswith(word):
            split = target[len(word):]
            numberOfWays = countConstruct(split,wordbank)
            totalCount += numberOfWays

    return totalCount

# print(countConstruct("purple",["purp","p","ur","le","purpl"]))

def countConstructTabulation(target,wordbank):
    table = [0] * ( len(target) + 1)
    table[0] = 1

    for i in range(len(target)+1):
        for word in wordbank:
            if word == target[i:i+len(word)] and i+len(word) < len(target)+1:
                table[i+len(word)] += table[i]
    return table[len(target)]

print(countConstructTabulation("purple",["purp","p","ur","le","purpl"]))
