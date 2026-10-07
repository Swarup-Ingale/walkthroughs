class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        level = {s}
        
        while True:
            valid_strings = [string for string in level if is_valid(string)]

            if valid_strings:
                return valid_strings

            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        new_string = string[:i] + string[i+1:]
                        next_level.add(new_string)

            level = next_level