
# def howSum(targetSum, array):
    # if targetSum == 0:
        # return list()
    # if targetSum < 0:
        # return None

    # for number in array:
        # remainder = targetSum - number
        # resultant = howSum(remainder,array)
        # if resultant is not None:
            # # (return resultant.append(number)) -> None,
            # # you need to return the resultant
            # resultant.append(number)
            # return resultant # Also resultant + [number] join two array
    # return None

isPrint = False
def howSum(targetSum, array, memo = {}):
    if isPrint:
        return memo
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return list()
    if targetSum < 0:
        return None

    for number in array:
        remainder = targetSum - number
        resultant = howSum(remainder,array,memo)
        if resultant is not None:
            # (return resultant.append(number)) -> None,
            # you need to return the resultant
            resultant.append(number)
            memo[targetSum] = resultant
            return resultant # Also resultant + [number] join two array
    memo[targetSum] = None
    return None

# print(howSum(7,[2,3]))
# isPrint = True
# Memo in cached in last call used in next function call, what
# https://docs.python-guide.org/writing/gotchas/
# print(howSum(7,[2,4]))

# Tabulation

def howSumTabulation(targetSum,array):
    table = [ None ] * (targetSum+1)
    table[0] = []
    for i in range(targetSum+1):
        if table[i] != None:
            for j in array:
                if i+j < targetSum+1:
                    table[i+j] = table[i] + [j]
    # print(table)
    return table[targetSum]

print(howSumTabulation(7,[2,3])) #[3,2,2]
print(howSumTabulation(7,[5,3,4,7])) #[4,3]
print(howSumTabulation(7,[2,4])) # None
print(howSumTabulation(8,[2,3,5])) # [2,2,2,2]
print(howSumTabulation(300,[7,14])) # None
