
def is_even(num) -> bool:
    if num == 0:
        return True
    elif num == 1:
        return False
    else:
        is_even(num-2)

print(is_even(55))
print(4)
