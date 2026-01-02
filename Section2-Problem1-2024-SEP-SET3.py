def last_word_starts_with_upper_case(sentence: str):
    """
    Find the last word in a sentence that starts with an uppercase letter.

    Args:
        sentence (str): The input sentence.

    Returns:
        str or None: The last word starting with an uppercase letter, or None if no such word exists.
    """
    
    
    last_word = None
    for word in sentence.split():
        if word[0].isupper():
            last_word = word
    return last_word

# #Another Method:
# def last_word_starts_with_upper_case(sentence: str):
#     l=[]
#     word=''
#     l=sentence.split()
#     for i in l:
#         if 65<=ord(i[0])<=90:
#             word=i
#     if word == '':
#         return None
#     else:
#         return word

# Last Word in a Given Sentence That Starts with Uppercase Letter
# Given a sentence, find the last word that starts with an uppercase letter. If no such word exists, return None. Words in the sentence are separated by spaces. Assume no punctuations will be present.

# Example

#     • "This is a Test sentence" --> "Test" last word that starts with an uppercase letter.

# "no uppercase words here", the result should be None.

# Explanation

#     • Words are separated by spaces, so we split the sentence into words.

#     • We check each word to see if it starts with an uppercase letter.

#     • We keep track of the last word that meets this condition.
    
