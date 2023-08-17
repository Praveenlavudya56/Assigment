def isValidParenthesis(s):
    stack = []
    mapp = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    for bracket in s:
        if bracket in mapp:
            topElement = stack.pop() if stack else '#'
            if mapp[bracket] != topElement:
                return False
        else:
            stack.append(bracket)
    return not stack

string = "(){()}[]]"
print(isValidParenthesis(string))  # Output will be False
