
def canConstruct(target, wordbank):
    if target == '':
        return True

    for word in wordbank:

        if target.startswith(word):
            split = target[len(word):]
            if canConstruct(split,wordbank):
                return True

    return False


def canConstruct(target, wordbank, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True

    for word in wordbank:

        if target.startswith(word):
            split = target[len(word):]
            memo[target] = canConstruct(split,wordbank,memo)
            if memo[target]:
                return True

    memo[target] = False
    return False

def canConstructTabulation(target,wordbank):

    table = [False] * (len(target)+1)
    table[0] = True

    for i in range(len(target)+1):

        if table[i]:
            for word in wordbank:
                if word == target[i:i+len(word)] and i+len(word) < len(target)+1:
                    table[i+len(word)] = True
    return table[len(target)]

print( canConstructTabulation("abcdef",["ab","abc","cd","def","abcd"] ))
print( canConstructTabulation("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e","ee","eee","eeee","eeeee"] ))
