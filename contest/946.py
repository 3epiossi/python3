class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        def dfs(rest, stack, result):
            if len(result) == len(popped):
                return True if result == popped else False
            
            outcome = False
            if stack:
                result.append( stack.pop() )
                outcome = outcome or dfs( rest, stack, result )
                stack.append( result.pop() )
            if rest:
                stack.append( rest.pop(0) )
                outcome  = outcome or dfs( rest, stack, result )
                rest.insert( 0, stack.pop() )
            return outcome
        return dfs( pushed, [], [])