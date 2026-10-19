class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m_end_val = 0
        i = 0
        while i <= m_end_val:
            m_end_val = max(m_end_val, i+nums[i])
            if m_end_val >= len(nums)-1:
                return True
            i += 1
        return m_end_val >= len(nums)-1