def balanced_paranthesis(input):

    stack = []

    pairs = {')' : '(',
             ']' : '[',
             '}' : '{'}

    for i in input:
        if i in '{[(':
            stack.append(i)
        elif i in ']})' and pairs[i] == stack[-1]:
            stack.pop()
        elif i in '}])' and pairs[i] != stack[-1]:
            return False
    return len(stack) == 0

input = 'a * {b + [c - d/ (e)]}'

print(balanced_paranthesis(input))
