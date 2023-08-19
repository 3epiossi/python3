class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        while popped :
            try :
                if stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
                else:
                    stack.append( pushed.pop(0) )
            except IndexError:
                try:
                    stack.append( pushed.pop(0) )
                except IndexError:
                    break
        return False if stack else True