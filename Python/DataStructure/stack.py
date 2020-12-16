
class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def top(self):

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):

        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def debug(self):
        return self._data

customStack = ArrayStack()
customStack.push(45)
customStack.push(46)
customStack.push(43)
print(customStack._data)
print(f"{customStack.pop()} data is poped")
print(f"{customStack.pop()} data is poped")
print(customStack._data)

# Applications

# Reversing the string

def reverse_file(filename):

    customStack = ArrayStack()
    original = open(filename)
    for line in original:
        customStack.push(line.rstrip('\n'))
    original.close

    output = open(filename, 'w')
    while not customStack.is_empty():
        output.write(customStack.pop() + '\n')
    output.close()

# Bracket Matching

def is_matched(expression):

    left_brackets = '({['
    right_brackets = ')}]'
    customStack = ArrayStack()
    for character in expression:
        if character in left_brackets:
            customStack.push(character)
        elif character in right_brackets:
            if customStack.is_empty():
                return False
            if right_brackets.index(character) != left_brackets.index(customStack.pop()):
                return False
    return customStack.is_empty()

print(is_matched('()(()){([()])}'))
print(is_matched(')(()){([()])}'))
