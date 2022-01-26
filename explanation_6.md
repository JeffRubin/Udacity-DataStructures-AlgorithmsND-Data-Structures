# Problem 6: Union And Intersection

## Overview
Converted the input linked lists into dictionaries for fast comparison and to eliminate duplicates (since dictionary
keys are unique).  For union, combined the resulting dictionaries (which also eliminated duplicates between the
dictionaries) and for intersection identified values that were in both dictionaries by iterating through one of the
dictionaries and testing whether the elements were in the other dictionary.  Converted union and intersection
dictionaries back to linked lists to return.

## Time Complexity: O(n)
For input linked lists of length x and y in the worst case where there are no duplicates within an input linked
(worst case since duplicates are removed):
- To convert the linked lists to dictionaries requires O(x) and O(y) since all elements of the input lists need to be
traversed; those are both thus O(n).
- For union, have to traverse all the elements of the dictionary being copied (e.g. if copying dictionary 2 into
dictionary 1, have to traverse all the elements of dictionary 2).  Thus, that's either O(x) or O(y) which is O(n).
Then, have to traverse all the elements of the combined dictionary to create the final linked list; in the worst case 
where the input linked lists are entirely different that's O(x+y) which is O(n). 
- For intersection, have to traverse all elements of one of the dictionaries; checking if the element is in the other
dictionary is O(1).  Thus, for traversal that's either O(x) or O(y) which is O(n).
- Overall, all time complexities are linear so the combined time complexity for both union and intersection 
is linear O(n)

## Space Complexity: O(n)
For input linked lists of length x and y in the worst case where there are no duplicates within an input linked
(worst case since duplicates are removed):
- To convert the linked lists to dictionaries requires O(x) and O(y) since all elements of the input lists need to be
traversed; those are both thus O(n).
- For union, the combined dictionary and linked list are O(x+y) which is O(n).
- Maximum intersection occurs when the input linked lists are equal and thus x = y so the dictionary and linked list
for intersection are O(x) = O(y) = O(n).
- Overall, all space complexities are linear so the combined space complexity for both union and intersection is
linear O(n)
