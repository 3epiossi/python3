class Solution:
    def decodeString(self, s: str) -> str:
        import string
        stack = []
        numStack = []
        num = ''
        numStart = 0
        i = 0
        while i < len(s):
            if s[i] in string.digits:
                num += s[i]
                i += 1
            elif s[i] == '[':
                stack.append( (int(num), i, numStart) )
                num = ''
                i += 1
                numStart = i
            elif s[i] == ']':
                repeat, left, frontest = stack.pop()
                front = s[:frontest]
                middle = s[left+1:i]
                rear = s[i+1:]
                s = front + repeat*middle + rear
                i = frontest
                while i < len(s) and s[i] in string.ascii_lowercase:
                    i += 1
                numStart = i
            else:
                i += 1
                numStart = i
        return s