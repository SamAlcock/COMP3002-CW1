# Q1a Pallidrome

def pallindrome_q1a(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return pallindrome_q1a(word[1:-1])
    
    return False

word = "madam"
if pallindrome_q1a(word):
    print(word + " is a pallindrome")
else:
    print(word + " is not a pallindrome")

# Q1b Generate all possible permutations of an array

def all_permutations_1b(arr):
    if len(arr) <= 1:
        return arr
    arr[0], arr[1] = arr[1], arr[0]
    print(arr)
    return all_permutations_1b(arr[1:])

arr = [1, 2, 3]
# all_permutations_1b(arr)

# Q1c LCM and GCD
def lcm_gcd_1c(nums):
    if len(nums) <= 1:
        return nums
    elif nums[0] == 0:
        return lcm_gcd_1c(nums[1:])
    else:

        nums[1] = nums[1] % nums[0]
        nums[0], nums[1] = nums[1], nums[0]
        return lcm_gcd_1c(nums)

nums = [46, 64, 578]
print("GCD = " + str(lcm_gcd_1c(nums)))
# Q1d Decimal to binary

def decimal_binary_1d(num):
    if num == 0 or num == 1:
        return num
    else:
        return str(decimal_binary_1d(num // 2)) + str(num % 2)

print(decimal_binary_1d(52))
