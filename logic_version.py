def isValid(brackets) :
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}

    for char in brackets:
        # if opening bracket
        if char in "({[":
            # push on top of the stack
            stack.append(char)
        # if closing bracket
        elif char in ")}]":
            # if the stack is empty or the current char is not
            # does not match the last char added to the top of the stack
            if not stack or stack[-1] != pairs[char]:
                return False
            # else pop the last item from the stack
            stack.pop()
        # Just in case an invalid character is input
        else:
            print("Invalid Character Included!")
    # if stack is empty then valid
    return len(stack) == 0

def main() :
    print(isValid("()[]{}")) #valid
    print(isValid("([)]")) #invalid
    print(isValid("({[]})")) #valid
    print(isValid("([]}")) #invalid
    print(isValid("(){}")) #valid

if __name__ == "__main__":
    main()