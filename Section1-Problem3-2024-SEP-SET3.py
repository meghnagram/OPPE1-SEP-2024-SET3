def increment_value_with_max_limit(d: dict, key: str, inc: int, limit: int):
    '''
    Increment the value for the given key in the 
    dictionary by `inc`, but not beyond `limit`.

    Modify the value in the dictionary do not return the new value.

    Args:
        d : dict - dictionary with integer values
        key : str - key to increment in the dictionary
        inc : int - increment value
        limit : int - maximum limit for the value

    Returns:
        None
    '''
    
    d[key] = min(d[key]+inc, limit)

# #Another Method:
# def increment_value_with_max_limit(d: dict, key: str, inc: int, limit: int):
#     a=d[key]
#     if a+inc > limit:
#         a=limit
#     else:
#         a=a+inc
    
#     d[key]=a

# Increment Value of Key in Dict with Max Limit
# Write a function increment_value_with_max_limit that increments the value for a specified key in a dictionary by a given increment value(inc). However, the value should not exceed a specified maximum limit (limit).

# Assume the dictionary values are integers. If the resulting value after incrementing is greater than the limit, it should be capped at the limit.



# Example

# >>> d = {"x": 5, "y": 3, "z": 5}
# >>> key, inc, limit = "y", 5, 5
# >>> increment_value_with_max_limit(d, key, inc, limit)
# >>> d 
# {"x": 5, "y": 5, "z": 5} # 3+5=8 but max limit is 5

# >>> increment_value_with_max_limit(d, "z", 5, 11)
# >>> d
# {"x": 5, "y": 5, "z": 10} # 5+5=10 less than limit

# >>> increment_value_with_max_limit(d, "x", 5, 4)
# >>> d
# {"x": 4, "y": 5, "z": 10} # 4+5=9 less than limit
