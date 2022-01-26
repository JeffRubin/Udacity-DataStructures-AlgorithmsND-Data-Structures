import sys
import heapq
import math

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def is_leaf(self):
        return (self.left is None and self.right is None)

    # operator overloads needs for heapq
    def __lt__(self, other):
        return self.frequency < other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

def find_huffman_codes(node, code_so_far):
    codes = dict()

    if node is None:
        return codes

    if node.is_leaf():
        codes[node.character] = code_so_far
    else:
        left_codes = find_huffman_codes(node.left, code_so_far + '0')
        codes.update(left_codes)
        right_codes = find_huffman_codes(node.right, code_so_far + '1')
        codes.update(right_codes)

    return codes

def huffman_encoding(data):
    # build a table of frequencies
    frequency = dict()
    for c in data:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    if len(frequency) < 1: # No data to encode
        return (data, None)

    # build a min heap to organize the table of frequencies
    # https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
    h_tree = list()
    heapq.heapify(h_tree)
    for e in frequency:
        new_node = Node(e, frequency[e])
        heapq.heappush(h_tree, new_node)

    # combine the min heap into a huffman tree
    while len(h_tree) > 1:
        min1 = heapq.heappop(h_tree)
        min2 = heapq.heappop(h_tree)
        new_combined_node = Node(None, min1.frequency + min2.frequency)
        new_combined_node.left = min1
        new_combined_node.right = min2
        heapq.heappush(h_tree, new_combined_node)

    # build a dictionary of huffman codes
    h_codes = find_huffman_codes(h_tree[0], '')

    # case where there is data to encode but not enough data to build a huffman tree (only 1 unique character in data)
    if(len(h_codes) == 1):
        h_codes[data[0]] = '0' # use 0 to encode

    # encode
    encoded_data = ""
    for c in data:
        encoded_data += h_codes[c]

    return (encoded_data, h_tree[0])

def huffman_decoding(data, tree):
    if tree is None: # this would occur if there was no data to encode
        return data

    decoded_data = ""

    # case where there is data to encode but not enough data to build a huffman tree (only 1 unique character in data)
    if tree.is_leaf():
        decoded_data = tree.character * len(data)
        return decoded_data

    cur_node = tree

    for c in data:
        if c == '0':
            cur_node = cur_node.left
        elif c == '1':
            cur_node = cur_node.right
        else:
            raise ValueError(f"Invalid encoded data value: {c}")

        if cur_node.is_leaf():
            decoded_data += cur_node.character
            cur_node = tree

    return decoded_data

def test_driver(to_encode):
    print("The size of the data is: {}".format(sys.getsizeof(to_encode)))
    print("The content of the data is: {}".format(to_encode))

    encoded_data, tree = huffman_encoding(to_encode)

    if tree is None: # encoding did not take place
        print(f"Encoding did not occur - Was unable to build a Huffman Tree")
    else:
        print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
        print("The content of the decoded data is: {}".format(decoded_data))

# Test Cases

##########
# Test Case 1: Nominal Encoding Via Huffman Coding
print('Test Case 1')
test_driver('AAAAAAABBBCCCCCCCDDEEEEEE')
# Expected Output:
# Encoded Size: Smaller than original size since encoding compresses the data (efficiently in this case since there are repeated characters)
# Encoded Content: 1010101010101000100100111111111111111000000010101010101
# Decoded Size: Same as original size (lossless compression)
# Decoded Content: AAAAAAABBBCCCCCCCDDEEEEEE
print('----------')

# Test Case 2: No Repeated Characters (Frequency Of All Characters Is 1)
print('Test Case 2')
test_driver('abcde')
# Expected Output:
# Encoded Size: Smaller than original size since encoding compresses the data (not as efficiently in this case since there are no repeated characters)
# Encoded Content: Every letter is a different code: a = 110, b = 10, c = 111, d = 01, e = 00
# Decoded Size: Same as original size (lossless compression)
# Decoded Content: abcde
print('----------')

# Test Case 3: Huffman Coding Not Possible - Encode Empty String
print('Test Case 3')
test_driver('')
# Expected Output:
# Encoding did not occur
print('----------')

# Test Case 4: Huffman Coding Not Possible - Encode Insufficient Unique Characters
print('Test Case 4')
test_driver('aaaaa')
# Expected Output:
# Encoded Size: Smaller than original size since encoding compresses the data (efficiently in this case since there are repeated characters)
# Encoded Content: 00000
# Decoded Size: Same as original size (lossless compression)
# Decoded Content: aaaaa
