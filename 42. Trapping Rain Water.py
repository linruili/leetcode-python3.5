class Solution(object):

    def trap(self , height):
        """
        :type height: List[int]
        :rtype: int
        """
        def trap(self, A):
            maxl, maxr, maxv, ans = [], [], 0, 0
            for i in range(len(A)):
                if A[i] > maxv: maxv = A[i]
                maxl.append(maxv)
            maxv = 0
            for i in range(len(A) - 1, -1, -1):
                if A[i] > maxv: maxv = A[i]
                maxr.append(maxv)
            for i in range(len(A)):
                minh = min(maxl[i], maxr[len(A) - i - 1]) - A[i]
                ans += minh if minh > 0 else 0
            return ans






