

# def canSum(targetSum, array):
    # if targetSum < 0:
        # return False
    # if targetSum == 0:
        # return True
    # for number in array:
        # remainder = targetSum-number
        # if canSum(remainder,array) == True:
            # return True
    # return False

# Memoization
# def canSum(targetSum, array,memo = {}):
    # if targetSum in memo:
        # return memo[targetSum]
    # if targetSum < 0:
        # return False
    # if targetSum == 0:
        # return True
    # for number in array:
        # remainder = targetSum-number
        # memo[targetSum] = canSum(remainder,array,memo)
        # if memo[targetSum]:
            # return True
    # memo[targetSum] = False
    # return False

# Tabulation
def canSum(targetSum,array):
    table = [ False ] * (targetSum+1)
    table[0] = True

    for i in range(targetSum+1):
        if table[i]:
            for num in array:
                if i+num <= targetSum:
                    table[i+num] = True

    return table[targetSum]

print(canSum(7,[2,3]))    # True
print(canSum(7,[5,3,4,7]))# True
print(canSum(7,[2,4]))    # False
print(canSum(8,[2,3,5]))  # True
print(canSum(300,[7,14])) # False
