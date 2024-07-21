class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lst = path.split('/')
        
        for c in lst:
            print(c)
            if c == "." or not c:
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            
            else:
                stack.append(c)

        print(stack)
        ans = "/" + "/".join(stack)

        return ans
        