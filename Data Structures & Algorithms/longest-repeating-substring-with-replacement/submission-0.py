class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        window = collections.defaultdict(int)
        i = 0
        j = 0
        while i < len(s):
            window[s[i]] += 1
            m_char = s[i]
            m_val = 1
            for key, val in window.items():
                if val > m_val:
                    m_val = val
                    m_char = key
            
            if i - j + 1 - window[m_char] > k:
                window[s[j]] -= 1
                j += 1
                
            res = max(res, i-j+1)
            i += 1
        return res