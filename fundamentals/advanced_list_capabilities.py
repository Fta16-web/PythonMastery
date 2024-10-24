'''
lists in python -> most basic collection class 
                -> variables have no type except through assignment 
                -> recommended to use suggestive variables name ex: my_int_list = [1,2,3,4]
                -> you can also create lists that mix numeric and string data ex:mixed_list = [10, 'fred', 5.3]  
                   usually not recommended some methods like sort can not executed 
                -> you can build collections by appending one element at a time to starting an empty list 
                   my_int_list = []
                   my-int_list.append(1) adds 1 to the end 
                   my-int_list.append(11) ...
                -> you can remove elements of list using .remove('item') method 
                   if item is not in the list ->value error exception is raised
                   .remove(item) removes only first instance of of item
                   
                -> copying list vs copying list variables 
                   variables are like more reference in c++ 
                   a_list = [2, 5, 10]
                   b_list = a_list # creates no data/ Make “b_list” an alias for whatever “a_list” refers to.
                   to create a separate copy of all the elements of a list, you need to perform a member-by-member copy.
                   b_list = a_list[:] using slicing to perform a member-by-member copy
                -> lists are mutable 
                   you can change them 'in place' without creating an entirely new list 
                   you can change individual elements by making one of those elements the target of an assignment—something you can’t do with strings.
                -> Indexing:
                    --> nonnegative indexing 
                        zero_based ->Index 0 denotes the first element in the list/These indexes run from 0 to N-1
                        where N is the number of elements.
                    --> Negative Indexes
                        refer to an element by its distance from the end of the list.
                        An index value of –1 denotes the last element in a list, and –2 denotes the next-to -last element, and so on. 
                        The value –N denotes the first element in the list.
                        Negative indexes run from –1 to –N, in which N is the length of the list. 
                        a_list = [100, 200, 300, 400, 500, 600]
                        print(a_list[-1])     # Prints 600.
                        print(a_list[-3])     # Prints 400.    
                ->Indexing
                     for i in range(len(a_list)): // avoid
                         print(a_list[i])
                  -> efficient and natural way is avoid range function 
                     a_list = ['Tom','Dick','Jane']
                     for s in a_list:
                        print(s)
                  -> use  enumerate(iter, start=0)
                      function takes an iterable like list  and produces another iterable,
                      which is a series of tuples. Each of those tuples has the form (num, item)
                      list(enumerate(a_list, 1)) -> produce [(1, 'Tom'), (2, 'Dick'), (3, 'Jane')]
                      We can put this together with a for loop to produce the desired result.
                       for item_num, name_str in enumerate(a_list, 1):
                           print(item_num, '. ', name_str, sep='')   
                ->Getting Data from Slices
                    Whereas indexing refers to one element at a time, the technique of slicing produces a sublist from a specified range.
                    The sublist can range in size from an empty list to a new list having all the contents of the original list.
                    Positive and negative index numbers can be mixed together
                    list[beg:end]
                    All list elements starting with beg, up to but not including end.

                    list[:end]
                    All elements from the beginning of the list, up to but not including end.

                    list[beg:]
                    All elements from beg forward to the end of the list.

                    list[:]
                    All elements in the list; this operation copies the entire list, element by element.

                    list[beg:end:step]
                    All elements starting with beg, up to but not including end; but movement through the list is step items at a time.
                    With this syntax, any or all of the three values may be omitted. Each has a reasonable default value; 
                    the default value of step is 1.
                    The step argument can be positive or negative but cannot be 0. If step is negative, then the defaults for the other values change as follows:
                    The default value of beg becomes the last element in the list (indexed as –1).
                    The default value of end becomes the beginning of the list.
                    Therefore, the slice expression [::-1] produces a reversal of the original list.
                -> Assigning into Slices
                   lists are mutable, you can assign to elements in place. This extends to slicing.
                   The following restrictions apply to this ability to assign into slices:
                    -When you assign to a slice of a list, the source of the assignment must be another list or collection,
                    even if it has zero or one element.
                    -If you include a step argument in the slice to be assigned to, the sizes of the two collections—the slice assigned to
                    and the sequence providing the data—must match in size. If step is not specified, the sizes do not need to match. 


'''
candidate_list = ['Fred', 'Ben','Jane']
for item_num, name_str in enumerate(candidate_list,1):
    print(item_num,'.',name_str,sep=' ')
    
    
a_list = [1, 2, 5, 10, 20, 30]
b_list = a_list[1:3]      # Produces [2, 5]
c_list = a_list[4:]       # Produces [20, 30]
a_list = [100, 200, 300, 400, 500, 600]
b_list = a_list[2:5:2]      # Produces [300, 500]
rev_list = a_list[::-1]     #[600, 500, 400, 300, 200, 100]
my_list = [10, 20, 30, 40, 50, 60]
my_list[1:4] = [707, 777] #effect of deleting the range [20, 30, 40] and inserting the list [707, 777] in its place
print(my_list) #[10, 707, 777, 50, 60]
my_list = [1, 2, 3, 4]
my_list[0:0] = [-50, -40] #The effect is to insert new list items without deleting existing ones
print(my_list)     # prints [-50, -40, 1, 2, 3, 4]
print(my_list.pop()) # prints last item = 4 and removes it from list 
print(my_list) # [-50, -40, 1, 2, 3]
print(my_list.pop(1))# prints index item = -40 and removes it from list 
from collections import deque
customers = deque(['Danial', 'Fred', 'Sara'])
customers.append('Simon')
print(customers) # prints deque(['Danial', 'Fred', 'Sara', 'Simon'])
print(customers.popleft()) #prints Danial
print(customers) # prints deque(['Fred', 'Sara', 'Simon'])
customers.appendleft('Saeed')
print(customers) # prints deque(['Saeed', 'Fred', 'Sara', 'Simon'])
