def get_filter(criteria):
    if criteria == 'continuous':
        return lambda x: x[-3:].lower() == 'ing'
    if criteria == 'vowel_rich':
        return lambda x: len([c for c in x.lower() if c in 'aeiou'])>5
    if criteria == 'consonant_rich':
        return lambda x: len([c for c in x.lower() if c.isalpha() and c not in 'aeiou'])>5
    if criteria == 'sorted':
        return lambda x: "".join(sorted(x.lower())) == x.lower()

def get_words_by_criteria(words, criteria=None):
    """
    Filters words based on the given criteria.

    Args:
        words (list): List of words.
        criteria (str): The filter criteria.

    Returns:
        list: Filtered list of words matching the criteria, or None if invalid criteria.
    """
    
    
    filter_func = get_filter(criteria)
    if filter_func is not None:
        return list(filter(filter_func, words))
    
#Another method:

# def get_words_by_criteria(words, criteria=None):
#    l=[]
#     if criteria=='continuous':
#         for i in words:
#             j=i.lower()
#             if j.endswith("ing"):
#                 l.append(i)
#         return l
#     elif criteria=='vowel_rich':
#         for i in words:
#             c=0
#             for j in i:
#                 if j.lower() in ('a','e','i','o','u'):
#                     c=c+1
#             if c>5:
#                 l.append(i)
#         return l
#     elif criteria == 'consonant_rich':
#         for i in words:
#             c=0
#             for j in i:
#                 if j.lower() not in ('a','e','i','o','u'):
#                     c=c+1
#             if c>5:
#                 l.append(i)
#         return l
#     elif criteria=='sorted':
#         for i in words:
#             j=sorted(i.lower())
#             if "".join(j)==i.lower():
#                 l.append(i)
#         return l
#     else:
#         return None

# Word Filters
# Given a list of words (case-insensitive), filter the words based on specific criteria and return the result as a list in the same order as the input. The criteria are as follows:

#     • continuous: words that end with "ing" (case-insensitive)

#     • vowel_rich: words that contain more than 5 vowels (not equal to 5)

#     • consonant_rich: words that contain more than 5 consonants (not equal to 5)

#     • sorted: words where the letters are sorted in ascending order

# If any other criteria is given, return None.

# Note: You can use the string methods like isalpha and lower if needed.

# Example

# For the list ["running", "aeiobcdioe", "acc", "xyz", "BOTbot" , "BboOTt" ,"jumpiNg", "SPINNING", "alphabetical"]:

#     • continuous criteria will yield ["running", "jumpinNg", 'SPINNING']

#     • vowel_rich criteria will yield ["aeiobcdioe"]

#     • consonant_rich criteria will yield ["SPINNING", "alphabetical"]

#     • sorted criteria will yield ["acc", "xyz", "BboOTt"]

#Another method
