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

# List-2 
# count_evens
def count_evens(nums: List[int]) -> int:
    i = 0
    even_count = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            even_count += 1
        i += 1
    return even_count

# big_diff
def big_diff(nums: List[int]) -> int:
    return max(nums) - min(nums)

# centered_average
def centered_average(nums: List[int]) -> int:
    largest = max(nums)
    smallest = min(nums)
    nums.remove(largest)
    nums.remove(smallest)
    sum_of_nums = sum(nums)
    length_of_nums = len(nums) 
    mean = sum_of_nums / length_of_nums
    return int(mean)

# sum_13
def sum_13(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    else:
        i = 0
        list_sum = 0
        while i < len(nums):
            if nums[i] >= 13:
                i += 2
            else:
                list_sum += nums[i]
                i += 1

        return list_sum

# has_22
def has_22(nums: List[int]) -> bool:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == 2:
            if nums[i + 1] ==2:
                return True
            else: 
                i += 1
        else:
            i += 1
    return False

# lucky_13
def lucky_13(nums: List[int]) -> bool:
    i = 0
    while i < len(nums):
        if nums[i] == 1 or nums[i] == 3:
            return False
        else:
            i += 1
    return True

# sum_28
def sum_28(nums: List[int]) -> bool:
    two_count = 0
    i = 0
    while i < len(nums):
        if nums[i] == 2:
            two_count += 1
            i += 1
        else:
            i += 1
    if two_count == 4:
        return True
    else: 
        return False
    
# more_14
def more_14(nums: List[int]) -> bool:
    count_4 = 0
    count_1 = 0
    index = 0
    while index < len(nums):
        if nums[index] == 1:
            count_1 += 1
        elif nums[index] == 4:
            count_4 += 1
        index += 1

    if count_1 > count_4:
        return True
    else:
        return False
    
# only_14
def only_14(nums: List[int]) -> bool:
    index = 0
    while index < len(nums):
        if nums[index] == 1 or nums[index] == 4:
            index +=1
        else:
            return False
    return True

# is_everywhere
def is_everywhere(nums: List[int], val: int) -> bool:
    index = 0
    while index < len(nums) - 1:
        if nums[index] != val and nums[index + 1] != val:
            return False
        else:
            index += 1
    return True
