class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dic = defaultdict(list)
        dic['2'] = ['a', 'b', 'c']
        dic['3'] = ['d', 'e', 'f']
        dic['4'] = ['g', 'h', 'i']
        dic['5'] = ['j', 'k', 'l']
        dic['6'] = ['m', 'n', 'o']
        dic['7'] = ['p', 'q', 'r', 's']
        dic['8'] = ['t', 'u', 'v']
        dic['9'] = ['w', 'x', 'y', 'z']
        
        def backtrack(index, curr):
            if index == len(digits):
                ans.append("".join(curr))
                return
            
            for i in dic[digits[index]]:
                curr.append(i)
                backtrack(index + 1, curr)
                curr.pop()
                
        ans = []
        backtrack(0, [])
        return ans
                
        
        
        
        