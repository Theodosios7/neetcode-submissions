class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Set of valid bracket pairs
        valid_pairs = {'()', '[]', '{}'}
        # Iterate through each character in the string
        for char in s:
            # If it is an opening bracket, push it onto the stack
            if char in '({[':
                stack.append(char)
            # If it is a closing bracket
            else: # Check if stack is empty (no mathcing opening bracket)
                  # Or if the top opening bracket doesn't match with current closing bracket
                if not stack or stack[-1] + char not in valid_pairs:
                    return False
                # Valid matching paird found, remove the opening bracket from stack
                stack.pop()
        # All brackets are valid if stack is empty (all opening brackets were matched)
        return not stack         