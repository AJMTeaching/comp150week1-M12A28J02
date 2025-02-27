# ------------------------------------------------------------------------

# Lab 1
### Lab Exercise 1: Lists in Python

my_list = [1, 5, 'apple', 20.5] #1. Created a list with the givien values 
print(my_list[2])  #2 using indexing, printed the value of apple 
my_list.append(10) #3 Added the value 10 to the end of my_list 
print(my_list) #print updated list
my_list.remove(20.5)  #4 removed the number 20.5 from the end of the list 
print(my_list) #print updated list
my_list.reverse()  #5 reversed the order of my_list using the .reverse method 
print(my_list) #print updated list

### Lab Exercise 2: Dictionaries in Python
person = {'name' : 'john', 'age': 30, 'job': 'teacher'} #1 created a dictioanry 

print (person['job']) #2 printed the value corresponding to job key

person['city'] = 'paris' #3.a adds a new key-value pair 
print (person) #3.b prints the new dictioanry

del person["age"] #4.a deletes age key-value pair 
print(person) #4.b prints out new dict 

for key, value in person.items(): #5.a iterates through the person dictionary
    print (f"{key}: {value}") #5.b prints them out 

# Problem 1
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
def count_vowels( s : str) -> int: 
    vowels = "aeiouAEIOU" #indicates what vowels are 
    count = 0 # sets up a counter
    
    for char in s: #creates for loop that checkes each character
        if char in vowels: #Checks if he character is a vowel
            count += 1 #adds the counter 
    
    return count #returns the total count at the end








# Problem 2
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
def merge_lists(list1: list, list2: list) -> list:
    merged = []  # Initialize an empty list to store merged elements
    i, j = 0, 0  # Pointers for both lists

    # Compare elements from both lists and append the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:  # Append element from list1
            merged.append(list1[i])  
            i += 1  # Move the pointer in list1
        else:  
            merged.append(list2[j])  # Append element from list2
            j += 1  # Move the pointer in list2

    # Add remaining elements from list1 (if any)
    while i < len(list1):
        merged.append(list1[i])
        i += 1  

    # Add remaining elements from list2 (if any)
    while j < len(list2):
        merged.append(list2[j])
        j += 1 
    return merged  # Return the merged sorted list

# Problem 3
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
def word_lengths(words: list) -> list:
    lengths = []  # Initialize an empty list to store lengths
    for word in words:  # Iterate through each word in the list
        lengths.append(len(word))  # Append the length of each word
    return lengths  # Return the list of lengths

 #Problem 4
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
def reverse_string(s: str) -> str:
    reversed_str = ""  # Initialize an empty string
    for char in s:  # Iterate through each character
        reversed_str = char + reversed_str  # Prepend the character
    return reversed_str  # Return the reversed string

 #Problem 5
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.
def intersection(list1: list, list2: list) -> list:
    result = []  # Initialize an empty list to store intersection elements
    for item in list1:  # Iterate through each element in list1
        if item in list2 and item not in result:  # Check if item exists in list2 and is not a duplicate
            result.append(item)  # Append to result
    return result  # Return the intersection list





# -----------------------------------------------------------------------------


# Importing sys for test function
import sys


# Custom Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    msg = f"Test at line {linenum} {'PASSED' if did_pass else 'FAILED'}."
    print(msg)


# Function 1: count_vowels
def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.

    Parameters:
    - s (str): The input string

    Returns:
    - int: The number of vowels in the string
    """
    # TODO: Implement this function
    pass


# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)


# Function 2: merge_lists
def merge_lists(list1: list, list2: list) -> list:
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - list1 (list): The first sorted list
    - list2 (list): The second sorted list

    Returns:
    - list: A new sorted list containing all elements from list1 and list2
    """
    # TODO: Implement this function
    pass


# Unit Tests for merge_lists
def test_merge_lists():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    merged = merge_lists(list1, list2)
    test(merged == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])


# Function 3: word_lengths
def word_lengths(words: list) -> list:
    """
    Get the lengths of words in a list.

    Parameters:
    - words (list): The list of words

    Returns:
    - list: A list containing the lengths of the words
    """
    # TODO: Implement this function
    pass


# Unit Tests for word_lengths
def test_word_lengths():
    words = ["hello", "world", "python"]
    lengths = word_lengths(words)
    test(lengths == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])


# Function 4: reverse_string
def reverse_string(s: str) -> str:
    """
    Reverse a string.

    Parameters:
    - s (str): The input string

    Returns:
    - str: The reversed string
    """
    # TODO: Implement this function
    pass


# Unit Tests for reverse_string
def test_reverse_string():
    text = "python"
    reversed_text = reverse_string(text)
    test(reversed_text == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")


# Function 5: intersection
def intersection(list1: list, list2: list) -> list:
    """
    Find the intersection of two lists.

    Parameters:
    - list1 (list): The first list
    - list2 (list): The second list

    Returns:
    - list: The intersection of the two lists
    """
    # TODO: Implement this function
    pass


# Unit Tests for intersection
def test_intersection():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = intersection(list1, list2)
    test(result == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])


# Test Suite
def test_suite():
    print(f"Count Vowels Test Results:")
    test_count_vowels()
    print(f"Merge Lists Test Results:")
    test_merge_lists()
    print(f"Word Lengths Test Results:")
    test_word_lengths()
    print(f"Reverse String Test Results:")
    test_reverse_string()
    print(f"Intersection Test Results:")
    test_intersection()


test_suite()
