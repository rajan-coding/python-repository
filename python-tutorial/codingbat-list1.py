def first_last6(nums):
    if nums[0] == 6 or nums[len(nums)-1]==6:
        return True
    else:
        return False
 
def same_first_last(nums):
    if len(nums)>=1 and nums[0] == nums[len(nums)-1]:
        return True
    else:
        return False
    
def make_pi():
 return [3,1,4]

def common_end(a, b):
    return a[0]==b[0] or a[len(a)-1]==b[len(b)-1]

def sum3(nums):
    return nums[0] + nums[1] + nums[2]

# def rotate_left3(nums):
#     for i in nums:
#         print(i)

def reverse3(nums):
    nums.reverse()
    return nums

def max_end3(nums):
  if nums[0] > nums[2]:
      return [nums[0]]*3
  else:
      return [nums[2]]*3
  

def sum2(nums):
 if len(nums) >= 2:
    return nums[0]+nums[1]
 elif len(nums) == 0:
   return 0
 else: 
   return nums[0]


