class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       num_dict= {} #number and index saved dict

       for i,num in enumerate(nums):
        complement = target-num

        if complement in num_dict:
            return [num_dict[complement],i] #index return numbers
        num_dict[num]=i #curent number and index saved 
      
