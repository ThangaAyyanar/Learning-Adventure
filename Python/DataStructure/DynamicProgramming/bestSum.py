
def bestSum(targetSum,array):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None
    for element in array:
        remainder = targetSum - element
        remainderCombination = bestSum(remainder,array)

        if remainderCombination is not None:
            remainderCombination.append(targetSum)

            if shortestCombination is None or len(remainderCombination) < len(shortestCombination):
                shortestCombination = remainderCombination

    return shortestCombination


def bestSumTabulation(targetSum,array):
    table = [ None ] * (targetSum+1)
    table[0] = []
    for i in range(targetSum+1):
        if table[i] != None:
            for j in array:
                if i+j < targetSum+1:
                    if table[i+j] == None or table[i] == None or len(table[i+j]) > len(table[i] + [j]):
                        table[i+j] = table[i] + [j]
    # print(table)
    return table[targetSum]

# print(bestSum(7,[5,3,4,7]))
print(bestSumTabulation(7,[5,3,4,7]))
print(bestSumTabulation(8,[2,3,5]))
print(bestSumTabulation(8,[1,4,5]))
print(bestSumTabulation(100,[1,2,5,25]))

# [7]
# [3, 5]
# [4, 4]
# [25, 25, 25, 25]
