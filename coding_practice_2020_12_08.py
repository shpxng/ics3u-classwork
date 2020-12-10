# List-1
# first_last_6
def first_last_6(nums: List[int]) -> bool:
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False

# same_first_last
def same_first_last(nums: List[int]) -> bool:
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False
# make_pi
def make_pi() -> List[int]:
    return [3, 1, 4]
  
# common_end
def common_end(a: List[int], b: List[int]) -> bool:
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False
    
# sum_3
def sum_3(nums: List[int]) -> int:
    return nums[0] + nums[1] + nums[2]

# rotate_left_3
def rotate_left_3(nums: List[int]) -> List[int]:
    return [nums[1], nums[2], nums[0]]

# reverse_3
def reverse_3(nums: List[int]) -> List[int]:
    return [nums[2], nums[1], nums[0]]

# max_end_3
def max_end_3(nums: List[int]) -> List[int]:
    if nums[0] > nums[-1]:
        return [nums[0]] * 3
    else:
        return [nums[-1]] * 3
    
# sum_2
def sum_2(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0
    else:
        return nums[0] + nums[1]
    
# middle_way
def middle_way(a: List[int], b: List[int]) -> List[int]:
    return [a[1], b[1]]

