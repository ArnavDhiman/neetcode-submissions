class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        alpha = "abcdefghijklmnopqrstuvwxyzABCDREFGHIJKLMNOPQRSTUVWXYZ0123456789"
        while i <= j:
            # print(s[i], s[j])
            if s[i] not in alpha:
                i += 1
            elif s[j] not in alpha:
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True