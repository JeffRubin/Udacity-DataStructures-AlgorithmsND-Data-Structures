# Problem 1: LRU Cache

## Overview
Used a dictionary for the cache to achieve quick lookup and sets for new values.
The value hashed by the dictionary is a node which is part of a doubly linked list where the least recently used node is
at the tail.  A double linked list is needed to be able to update the links when a node is accessed.
The linked list made identifying and removing the least recently used node very quick. 

## Time Complexity: O(1)
O(1) since the cache is a dictionary with lookups/sets at O(1) and the logic to track the
oldest item is a doubly linked list where operations to keep the links up-to-date are O(1) and the nodes of linked list
are hashed via the cache dictionary such that no searching is required to find the oldest item (it's at the tail of the
linked list).

## Space Complexity: O(n)
O(n) where n is the capacity of the cache.  When the cache is full, the dictionary holds up to n elements and the linked
list has n nodes.  That's 2n which is approximately n for large n.

## Other Notes
I had a really difficult time with this problem and needed some help.  In particular, I identified that a linked
list would be useful to track the oldest item since the nodes could be freely rearranged to place the oldest at the tail
but I couldn't figure out how to avoid searching through the linked list for an accessed item, i.e. I didn't think to
hash the nodes via the cache dictionary.  Thus, I needed some help and used:
https://www.geeksforgeeks.org/lru-cache-implementation/

The only part of the website that I read was the first 2 items of the section:
"We use two data structures to implement an LRU Cache"  Those items list that a doubly linked list and hash are a
useful approach.  I was able to take that direction and work towards a solution.  I did not look at or use any code
from the website.
