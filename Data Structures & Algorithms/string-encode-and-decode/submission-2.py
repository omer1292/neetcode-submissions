class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths = []
        for i in strs:
            lengths.append(len(i))
        new = ""
        for i in strs:
            new += i
        new += "a"
        for i in lengths:
            new+=str(i)+"b"
        return new

    def decode(self, s: str) -> List[str]:
        l = s.rfind("a")
        lens = s[l+1:].split("b")
        st = 0
        out = []
        for i in lens:
            if i == "":
                continue
            i=int(i)
            out.append(s[st:st+i])
            st +=i
        return out
