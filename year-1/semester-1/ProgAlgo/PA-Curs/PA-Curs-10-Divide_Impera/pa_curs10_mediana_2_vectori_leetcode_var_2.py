class Solution:
    def getMedianBS(self,a,b,pa,ua): #a mai mic, in a cautam pe x
        n1, n2 = len(a), len(b)
        if pa<=ua:
            x = (pa + ua) // 2
            y = (n1 + n2 + 1) // 2 - x
            ax_1 = float("-inf") if x == 0 else a[x - 1] #bordam vectorii cu -∞, +∞
            by_1 = float("-inf") if y == 0 else b[y - 1]
            ax = float("inf") if x == n1 else a[x]
            by = float("inf") if y == n2 else b[y]
            if ax_1 <= by and by_1 <= ax:
                if (n1 + n2) % 2 == 0:
                    return (max(ax_1, by_1)+min(ax, by))/2
                else:
                    return max(ax_1, by_1)
            elif ax_1 > by:
                return self.getMedianBS(a,b,pa,x - 1)
            else:
                return self.getMedianBS(a,b,x+1,ua)

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        return self.getMedianBS(nums1,nums2,0,n1) #bordat vectorul cu inf - o pozitie in plus
