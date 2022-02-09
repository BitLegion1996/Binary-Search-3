class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l , r = 0 ,len(arr) - k
        while l < r:
            m = l + (r-l)//2
            if x - arr[m] > arr[m+k] - x:  # if element at mid + k is closer to x mode the left ptr
                l = m + 1
            else:                 # if element at mid is closer to x move right ptr 
                r = m 
        return arr[l:r+k]

        
        
'''
BINARY SEARCH APPROACH 
left --> 0 
right --> len(arr)-1
while left < right:
    m = left + (right-left)//2
    if the element at the mid point minus x greater than the 
    element at mid point + k minus x
                we adjust the left to m + 1
    else: 
                we adjust the right pointer to m 
finally we return the elements bounded by the left and the right pointer 

Time Complexity = O(logN)
Space Complexity = O(1)
        
'''
