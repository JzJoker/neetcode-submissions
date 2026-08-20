class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, td = defaultdict(int), defaultdict(int)
        for ch in t:
            td[ch] += 1

        have = 0
        need = len(td)
        resLen, res = float('inf'), [-1, -1]
        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1

            if ch in td and window[ch] == td[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in td and window[s[l]] < td[s[l]]:
                    have -= 1
                l +=1 
        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""
                