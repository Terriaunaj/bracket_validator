class BracketValidator:
    def __init__(self):
        # dictionary pairs
        self.pairs = {')':'(', '}':'{', ']':'['}
    
    def isValid(self, brackets: str) -> bool:
        stack = []

        for char in brackets:
            # if opening bracket
            if char in "({[":
                # push on top of the stack
                stack.append(char)
            # if closing bracket
            elif char in ")}]":
                # if the stack is empty or the current char is not
                # does not match the last char added to the top of the stack
                if not stack or stack[-1] != self.pairs[char]:
                    return False
                # else pop the last item from the stack
                stack.pop()
            # Just in case an invalid character is input
            else:
                print("Invalid Character Included!")
        # if stack is empty then valid
        return len(stack) == 0

def main() :
    validator = BracketValidator()
    print(validator.isValid("()[]{}")) #valid
    print(validator.isValid("([)]")) #invalid
    print(validator.isValid("({[]})")) #valid
    print(validator.isValid("([]}")) #invalid
    print(validator.isValid("(){}")) #valid

if __name__ == "__main__":
    main()