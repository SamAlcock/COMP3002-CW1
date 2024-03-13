# Q1a Pallidrome
# The solution for 1a works by firstly having a base case that checks if the length of the input is less than or equal to 1. If the word length is 0 or 1, then the word is always a
# pallindrome. If the conditions for this are not fufilled, then the recursion case checks for whether the first and last character of the word are the same. If this is true, then a
# recursive call is made. If this is not true, then the input word cannot be a pallindrome, so false is returned. The function will eventually return the final result when the word
# is broken down into 0 or 1 character. The computational complexity of this function is O(n), n is the length of the word input.


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
# The solution for 1b starts by checking whether the length of the array is 1. If this is the case, then the array is already sorted due to there only being 1 element or it has been reached due
# to recursion, which in that case means that all permutations have been found. If the array length is greater than 1 then the array is copied to keep the original for further iterations, then
# the first element is swapped with the ith element. A recursive call is made without the first element to get the rest of the permutations. After this, the newly generated permutations are
# appended to the results to be output once the break condition is reached. The computational complexity of this solution is O(n*n!), with n being the length of the array.

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
arr = [1, 2, 3, 4]

print(all_permutations_1b(arr))

# Q1c LCM and GCD
# The solution for 1c firstly calculates the GCD for all numbers in the array. The first if statement in 'gcd()' is the break condition for recursion. The next if statement checks whether the
# first element in the array is 0. If this is the case, a common denominator has been found. The element needs to be removed to avoid division by 0 and so that the next element can be used. 
# If neither of these conditions are fufilled, then the second element becomes the modulo of the first and second element, and are then swapped. A recursive call is then made. Once the GCD has
# been found, the LCM is found by finding the GCD of two elements at a time, and then using that to divide the result of the LCM of the pair of values, multiplied by the next element in the array.
# The computational complexity of this solution is O().
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
    
    def lcm(arr):

        lcms = arr[0]
        for i in range(len(arr) - 1):
            gcdenom = gcd([lcms, arr[i + 1]]) 
            lcms = lcms * arr[i + 1] // gcdenom[0]
        return lcms

    gcdenom = gcd(nums)
    lcmul = lcm(nums_copy)


    return lcmul, gcdenom

    


nums = [6, 12, 36]

l, g = lcm_gcd_1c(nums)
print("LCM = " + str(l) + ", GCD = " + str(g))

# Q1d Decimal to binary
# The solution for 1d works by firstly having a base case that checks for whether the input number is 0 or 1. If this is the case, then the decimal number is already the same as it would be
# in binary, so that can be returned as is. If this is not true, then the recursive case performs a recursive call with the input number, with a floor division of 2. The remainder is
# appended to the final result. This function will eventually return the final result once num has divided down to 0 or 1. The computational complexity of this function is O(log n).
 
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
# of an input array is less than or equal to 1. The computational complexity of this solution is dependent on the pivots chosen, but on average computational complexity should be O(n log n). 
import random 
def quick_sort_1e(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_idx = random.randint(0, len(arr) - 1)
    less = [x for x in arr if x < arr[pivot_idx]]
    equal = [x for x in arr if x == arr[pivot_idx]]
    greater = [x for x in arr if x > arr[pivot_idx]]
    return quick_sort_1e(less) + equal + quick_sort_1e(greater)
        
arr = [2,6,2,4,7,8,6]
print(quick_sort_1e(arr))

# Q1f Bubble sort
# The solution for 1f starts with an if statement checking if the arr length is less than or equal to 1. This is for the recursion break condition, and if the input array is a length of 0 or 1.
# In a scenario where this is true, then the array is already sorted. After this check, a loop occurs and an if statement checks for whether the first element is larger than the ith element. If
# this is true then the elements are swapped. Once the loop has finished, the smallest element will be in the correct position. Recursive calls can then be made with the rest of the array until
# it has been fully sorted. The computational complexity of this solution is O(n^2), n is the length of the array.

def bubble_sort_1f(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)):
        if arr[0] > arr[i]:
            arr[0], arr[i] = arr[i], arr[0]


    return [arr[0]] + bubble_sort_1f(arr[1:])


print(bubble_sort_1f(arr))


# Q3 Monadic type
import math;
def q3_monads():
    dictionary = {}
    def unit(num1, num2):
        return(num1, num2, "Ops: ")

    def bind(t, f):
        res = f(t[0], t[1])
        return (res[0], t[-1] + res[1] + ";")

    def add(num1, num2):
        m = (num1 + num2, str(num1) + " + " + str(num2))
        add_to_dictionary(m)
        return m

    def subtract(num1, num2):
        m = (num1 - num2, str(num1) + " - " + str(num2))
        add_to_dictionary(m)
        return m

    def multiply(num1, num2):
        m = (num1 * num2, str(num1) + " * " + str(num2))
        add_to_dictionary(m)
        return m

    def divide(num1, num2):
        if num1 == 0 or num2 == 0:
            m = (1, "error, can't divide by 0")
            
        else:
            m = (num1/num2, str(num1) + " / " + str(num2))
        add_to_dictionary(m)
        return m 

    def f_sin(num1, num2):
        m = (math.sin(num1), "sin(" + str(num1) + ")")
        add_to_dictionary(m)
        return m

    def f_cos(num1, num2):
        m = (math.cos(num1), "cos(" + str(num1) + ")")
        add_to_dictionary(m)
        return m

    def f_sqrt(num1, num2):
        m = (math.sqrt(num1), "sqrt(" + str(num1) + ")")
        add_to_dictionary(m)
        return m

    def add_to_dictionary(m):
        dictionary[m[1]] = str(m[0])

    print((bind(unit(9, 2), f_sqrt)))
    print(dictionary)

q3_monads()