class Solution:
    def reverseVowels(self, s: str) -> str:
        vow=[]
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                vow.append(s[i])
        vow.reverse()
        ans=""
        c=-1
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                c+=1
                ans+=vow[c]
            else:
                ans+=s[i]
        return ans
        