
# Recursion
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)

# Dynamic programming - memoization
def dynfib(n,memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = dynfib(n-1,memo)+dynfib(n-2,memo)
    return memo[n]

# Tabulation
def tabfib(n):
    table = [0]*(n+1)
    table[1] = 1
    for i in range(n-1):
        table[i+1] += table[i]
        table[i+2] += table[i]
    table[n] += table[n-1]
    return table[n]

print(tabfib(6)) # 8
print(tabfib(7)) # 13
print(tabfib(8)) # 21
print(tabfib(50)) # 12586269025
