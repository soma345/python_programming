
import heapq
#class Solution(object):
def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Using the Max heap Time : O(N+Klogn)
        heap=[]

        for i in range(len(nums)):
            heap.heappush(nums[i])
        while k > 0 :
            min = heapq.heappop(heap)
                
        return min
    
    
  


    


        