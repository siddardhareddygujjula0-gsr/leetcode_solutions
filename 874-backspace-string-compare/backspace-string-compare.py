class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if stack and i == "#":
                stack.pop()
            elif i != '#':
                stack.append(i)
        st1 = []
        for j in t:
            if st1 and j == '#':
                st1.pop()
            elif j!='#':
             
                st1.append(j)
        return stack ==st1
        