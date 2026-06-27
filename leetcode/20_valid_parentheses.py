class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = {'{': '}',
                             '(': ')',
                             '[': ']'}
        pipeline_list = []
        for char in s:
            if char in parentheses_stack.keys():
                pipeline_list.append(parentheses_stack[char])
            else:
                if len(pipeline_list) == 0:
                    return False
                closing = pipeline_list.pop()
                if closing != char:
                    return False
        return True if len(pipeline_list) == 0 else False
