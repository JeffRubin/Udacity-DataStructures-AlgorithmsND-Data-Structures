# Problem 3: Huffman Coding

## Overview
- Used a dictionary to quickly determine the character frequencies for the input data (O(1) set and get).
- Used a min heap for a priority queue to build Huffman Tree since O(1) retrieval of the minimum value and O(log n) to
update the tree after adding or removing nodes.  Used python's built-in heapq for this.
This seemed more efficient than using an ordered linked list where retrieval of the minimum value would still be O(1)
but which could require O(n) to reorder after adding or removing nodes.
- Used recursion to traverse all paths in the Huffman Tree to determine Huffman Codes and stored these in a dictionary
for quick lookup.
- Included simple special logic when there is only 1 unique character in the input to encode; just encode as all 0s.
A Huffman Tree does not work in this situation since a Huffman Tree requires at least 2 unique characters.
- Implemented decoding by walking down the Huffman Tree.  Considered using a reverse dictionary to decode but decided
against this since encodings can be different lengths, e.g. 10, 111.  Even though Huffman Codes are prefix codes and
thus do not overlap, since encodings can be different lengths it was not clear how to determine where character breaks
occur in the encoded string without trying different lengths against a reverse dictionary; this did
not seem like a clean solution.

## Time Complexity: O(n log n)
O(n log n) where n is the number of characters in the input data to encode.
Dictionary operations for frequencies and Huffman Codes are O(1) and the min heap operations are O(1) for
minimum node retrieval and O(log n) for reordering for n inputs, so O(n log n).  Recursively following all paths of
the Huffman Tree (tree depth log n) for n unique inputs (worst case) was also O(n log n) to determine the Huffman Codes.
Many aspects of this algorithm are O(n) including: Building the frequency dictionary, building the Huffman Tree
from the min heap, encoding the input using the Huffman Codes, and decoding the encoded data. O(n log n) thus dominates.

## Space Complexity: O(n)
O(n) where n is the number of characters in the input data to encode since in the worst case there are n elements in the
frequency dictionary, min heap, and Huffman Codes dictionary (2n-1 for the last of these in the worst case which is
approximately n for large n).  Encoded data should be smaller or equal to the input data (only equal to if encoding is
not possible).  Recursion call stack is O(log n) to traverse the Huffman Tree.  Thus O(n) dominates.
