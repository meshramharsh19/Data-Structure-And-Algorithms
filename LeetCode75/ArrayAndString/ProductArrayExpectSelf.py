class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n 
        answer = [0] * n  
        
        # Calculate the prefix product
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
        
        # Calculate the suffix product
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
            
        for i in range(n):
            answer[i] = left_product[i] * right_product[i]
        
        return answer
