import string

def contains_punctuation(input_str):
    ''' Return True if the input_str contains punctuations.
    Return False otherwise'''
    for punctuation in string.punctuation:
        if punctuation in input_str:
            return True
    return False

def contains_punctuation_s(input_str):
    return any(char in string.punctuation
        for char in input_str
    )


