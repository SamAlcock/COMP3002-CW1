# Q1a Pallidrome
# The solution for 1a works by firstly having a base case that checks if the length of the input is less than or equal to 1. If the word length is 0 or 1, then the word is always a
# pallindrome. If the conditions for this are not fufilled, then the recursion case checks for whether the first and last character of the word are the same. If this is true, then a
# recursive call is made. If this is not true, then the input word cannot be a pallindrome, so false is returned. The function will eventually return the final result when the word
# is broken down into 0 or 1 character. The computational complexity of this function is O(n).

from itertools import permutations
from math import lcm


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
    result = []
    for i in range(len(arr)):
        arr_copy = arr.copy()
        arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]
        permutations = all_permutations_1b(arr_copy[1:])
        for j in range(len(permutations)):
            result.append(str(arr_copy[0]) + str(permutations[j]))

    
    return result
arr = [1, 2, 3, 4, 5]

print(all_permutations_1b(arr))

# Q1c LCM and GCD
def lcm_gcd_1c(nums):
    nums_copy = nums.copy()
    def gcd(nums):
        if len(nums) <= 1:
            return nums
        elif nums[0] == 0:
            return gcd(nums[1:])
        else:
            nums[1] = nums[1] % nums[0]
            nums[0], nums[1] = nums[1], nums[0]
            return gcd(nums)
    
    def lcm(arr, gcdenom):
        if len(arr) == 2:
            return arr[0] * arr[1] // gcdenom
        lcm_pair = arr[0] * arr[1] // gcdenom
        return lcm([lcm_pair] + arr[2:], gcdenom)



    gcdenom = gcd(nums)
    lcmul = lcm(nums_copy, gcdenom[0])


    return lcmul, gcdenom

    


nums = [2, 4, 10, 8]

l, g = lcm_gcd_1c(nums)
print("LCM = " + str(l) + ", GCD = " + str(g))

# Q1d Decimal to binary
# The solution for 1d works by firstly having a base case that cheks for whether the input number is 0 or 1. If this is the case, then the decimal number is already the same as it would be
# in binary, so that can be returned as is. If this is not true, then the recursive case performs a recursive call with the input number, with a floor division of 2. The remainder is
# appended to the final result. This function will eventually return the final result once num has divided down to 0 or 1. The computational complexity of this function is O(log n)
def decimal_binary_1d(num):
    if num == 0 or num == 1:
        return num
    else:
        return str(decimal_binary_1d(num // 2)) + str(num % 2)

print(decimal_binary_1d(52))

# Q1e Randomised Quick-Sort
# The solution for 1e works by firstly having a base case that checks for whether the length of the input array is 0 or 1. If this is the case, then the array is already sorted and can be
# returned. If this is not the case then a pivot is chose at random, and three arrays are created using list comprehension. Values in these three lists are based on whether they are less
# than, equal to, or greater than the pivot value. A recursive call is then made to sort both the less than and greater than lists. The sorted list will eventually be returned when the length
# of an input array is less than or equal to 1. The computational complexity of this solution is - 
import random 
def quick_sort_1e(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_idx = random.randint(0, len(arr) - 1)
    less = [x for x in arr if x < arr[pivot_idx]]
    equal = [x for x in arr if x == arr[pivot_idx]]
    greater = [x for x in arr if x > arr[pivot_idx]]
    return quick_sort_1e(less) + equal + quick_sort_1e(greater)
        
arr = [5, 6, 14, 1, 84, 3, 5, 1]
print(quick_sort_1e(arr))

# Q1f Bubble sort

def bubble_sort_1f(arr):
    if len(arr) <= 1:
        return arr

    arr = [x for x in arr if x < arr[0]]
    print(arr)
    return bubble_sort_1f(arr)

print(bubble_sort_1f(arr))


# Q3 Monadic type
def unit(num1 , num2):
    return(num1, num2, "Ops: ")

def bind(t, f):
    res = f(t[0], t[1])
    return (res[0], t[-1] + res[1] + ";")

def add(num1, num2):
    return (num1 + num2, str(num1) + " + " + str(num2))

def subtract(num1, num2):
    return(num1 - num2, str(num1) + " - " + str(num2))

def multiply(num1, num2):
    return(num1 * num2, str(num1) + " * " + str(num2))

def divide(num1, num2):
    if num1 == 0 or num2 == 0:
        return (1, "error")
    else:
        return(num1/num2, str(num1) + " / " + str(num2))


print(bind(unit(5, 2), divide))