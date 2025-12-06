# region Problem Statement

    # You are given a string 'STR'. You have to convert the first alphabet of each word in a string to UPPER CASE.

    # For example:

    # If the given string 'STR' = ”I am a student of the third year” so you have to transform this string to ”I Am A Student Of The Third Year"
    # Note:

    # 'STR' will contains only space and alphabets both uppercase and lowercase. The words will be separated by space.

#endregion

from os import *
from sys import *
from collections import *
from math import *

def convertString(str):
    result = []
    new_word = False

    for ch in str:
        if ch.isspace():#if ch in (' ','\n','\r\n','\r','\t'):
            result.append(ch)
            new_word = True
        else:
            if new_word:
                result.append(ch.upper())
                new_word = False
            else:
                result.append(ch)

    return ''.join(result)

# Test
input_str = "I am a student of the third year"
output_str = convertString(input_str)
print(output_str)  # Output: "I Am A Student Of The Third Year"

input_str2 = "I love programming they are playing cricket good to see you"
output_str2 = convertString(input_str2) 
print(output_str2)  # Output: "Hello World! This Is A Test."