def div_by_exactly_one(num: int, a: int, b: int) -> bool:
    '''Check if num is divisible by exactly one of a or b.

    Args:
        num, a, b : int - input numbers

    Returns:
        bool - True if num is divisible by exactly one of a or b, otherwise False.
    '''
    
    return (num % a == 0) ^ (num % b == 0)
  
# #Another method:
# if num%a==0 and not(num%b==0):
#         return True
#     elif not(num%a==0) and num%b==0:
#         return True
#     else:
#         return False

# Check if a Number is Divisible by Exactly One of the Given Numbers
# Write a function div_by_exactly_one that takes three integers num, a, and b. The function should return True if num is divisible by exactly one of the numbers a or b, and False otherwise.

# Examples:

#     • num=20, a=5, b=6 --> True (20 is divisible by 5 only)

#     • num=20, a=5, b=10 --> False (20 is divisible by both 5 and 10)

#     • num=20, a=6, b=10 --> True (20 is divisible by 10 only)

    • num=20, a=6, b=7 --> False (20 is not divisible by either 6 or 7)
