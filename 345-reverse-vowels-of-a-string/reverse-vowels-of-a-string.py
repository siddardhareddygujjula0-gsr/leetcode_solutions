class Solution:
    def reverseVowels(self, st: str) -> str:
        vow=[]
        for i in range(len(st)):
            if st[i] in "AEIOUaeiou":
                vow.append(st[i])
        vow.reverse()
        ans=""
        c=-1
        for i in range(len(st)):
            if st[i] in "AEIOUaeiou":
                c+=1
                ans+=vow[c]
            else:
                ans+=st[i]
        return ans
        
