class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.brute_force(nums1, nums2)

    def brute_force(self, nums1, nums2):
        i=j=k= 0
        res = 0.0
        total_len = len(nums1)+len(nums2)
        mid = (total_len)//2
        n1, n2 = 0,0
        while k <= mid:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    n1, n2 = n2, nums1[i]
                    i += 1
                else:
                    n1, n2 = n2, nums2[j]
                    j += 1
            elif i < len(nums1):
                n1, n2 = n2, nums1[i]
                i += 1
            elif j < len(nums2):
                n1, n2 = n2, nums2[j]
                j += 1
            k += 1
        # print(i,j,k,n1,n2)
        if total_len%2 == 0:
            return (n1+n2)/2
        else:
            return n2