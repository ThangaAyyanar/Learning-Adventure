

# def gridTraveler(n,m):
    # if n == 0 or m == 0:
        # return 0
    # if n == 1 and m == 1:
        # return 1
    # return gridTraveler(n-1,m) + gridTraveler(n,m-1)

# def gridTraveler(n,m,memo={}):
    # key = f"{n},{m}"
    # if key in memo:
        # return memo[key]
    # if n == 0 or m == 0:
        # return 0
    # if n == 1 and m == 1:
        # return 1
    # memo[key] = gridTraveler(n-1,m,memo) + gridTraveler(n,m-1,memo)
    # return memo[key]

# Tabulation
def gridTraveler(n,m):
    table = [ [0]*(m+1) for i in range(n+1)]

    table[1][1] = 1

    for i in range(n+1):
        for j in range(m+1):
            current = table[i][j]
            if j+1 <= m:
                table[i][j+1] += current
            if i+1 <= n:
                table[i+1][j] += current

    return table[n][m]


print(gridTraveler(1,1)) # 1
print(gridTraveler(2,3)) # 3
print(gridTraveler(3,2)) # 3
print(gridTraveler(3,3)) # 6
print(gridTraveler(18,18)) # 2333606220
