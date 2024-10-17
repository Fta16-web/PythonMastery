def str_comp_no_case(str1,str2):
    #the safest way to do case-insensitive comparisons is to use the casefold method instead of using  upper or lower string method
    return str1.casefold() == str2.casefold()



"""
---------------------------------------------------------
#    advantage of immutable types(string)
        1- can be used as a key in dictionary
        2- because they cannot be changed, their usage is optimized internally.
my_str = 'hello, Dave, this is Hal.'
my_str[0] = 'H'      TypeError: 'str' object does not support item assignment
  Strings are immutable ->such data cannot be changed in place
  Mutable types include lists, dictionaries, and sets.  
--------------------------------------------------------------
#   String Operators (+, =, *, >, etc.)
    -All operator-based comparisons with Python strings are case-sensitive
    -As long as two strings have the same content, they are considered equal.
     They do not necessarily have to be aliases for the same data in memory.
    dog_1 = 'Rex'
dog_2 = dog_1 # creating alias
print(dog_1 ==dog_2)  #True
print(dog_2 == 'Rex') #True
print(dog_1 == 'Rex') #True
print(str_comp_no_case('rex',dog_1)) #True
-----------------------------------------------------------------------
When should you use is or is not?
    - These operators test for whether or not two values are the same object in memory
    -  use them primarily when you’re comparing objects of different types, for which the appropriate test for equality (==)
       might not be defined. One such case is testing to see whether some value is equal to the special value None, which is 
       unique and therefore appropriate to test using is.  
    - 
----------------------------------------------------------------------
  extracting  data from string:
  You cannot use indexing, slicing, or any other operation to change values of a string “in place,” because strings are immutable.
  ### indexing:
       -uses a number to refer to an individual character, according to its place within the string.
       -
  ### slicing:  Slicing is an ability more unique to Python. It enables you to refer to an entire 
      substring of characters by using a compact syntax.Slicing is a special ability shared by Python strings, lists, and tuples
      -positive indexes run from 0 to N–1, where N is the length of the string.
      -negative indexes, which run backward from –1 (indicating the last character) to –N.
      -string[beg: end] ->All characters starting with beg, up to but not including end.
      -string[:end] -> All characters from the beginning of the string up to but not including end.
      -string[beg:] -> All elements from beg forward to the end of the string.
      -string[:] -> All characters in the string; this operation copies the entire string.
      -string[beg: end: step] ->All characters starting with beg, up to but not including end, moving through the string step items at a time.
      -
      -
 Note: Python has no separate “character” type.ex: print(type('g')) returns <class 'str'>
  ------------------------------------  
"""
divider_str = '_' * 30
print(divider_str)
cat_1 = 'Meyo'
cat_2 = 'Meyo2'
print(cat_1 ==cat_2)





