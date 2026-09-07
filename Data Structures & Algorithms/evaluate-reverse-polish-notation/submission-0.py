class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = { "+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            
            else:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left*right
                elif token == "/":
                    result = int(left/right)
                
                stack.append(result)
        
        return stack[-1]
