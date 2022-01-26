import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        # all members are strings except next which is a link to the next Block for a linked list
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        to_hash = self.timestamp + self.data + self.previous_hash
        hash_str = to_hash.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        timestamp = time.strftime("%I:%M %d %b %Y", time.gmtime()) # format is hh:mm dd mon yyyy
        if self.tail is None:
            previous_hash = '0'
        else:
            previous_hash = self.tail.hash
        new_block = Block(timestamp, data, previous_hash)

        if self.tail is None:
            self.head = new_block
            self.tail = new_block
        else:
            self.tail.next = new_block
            self.tail = new_block

    def verify_chain(self):
        cur_block = self.head
        prev_block = None

        while cur_block:
            if prev_block is not None: # non-first block
                if cur_block.previous_hash != prev_block.hash:
                    print(f"Current block (data: {cur_block.data}), has a different hash ({cur_block.previous_hash}) " \
                          f"for the previous block (data: {prev_block.data}), than the previous block has for " \
                          f"itself ({prev_block.hash})\n")

                    return False

            recalculated_hash = cur_block.calc_hash()
            if cur_block.hash != recalculated_hash:
                print(f"Current block (data: {cur_block.data}), has a stored hash ({cur_block.hash}) " \
                      f"that does not match the hash that results if the hash for this block is recalculated " \
                      f"({recalculated_hash})\n")

                return False

            prev_block = cur_block
            cur_block = cur_block.next

        return True

    def __str__(self):
        output = "\n"

        cur_block = self.head

        while cur_block:
            output += "data: " + cur_block.data + "\n"
            output += "timestamp: " + cur_block.timestamp + "\n"
            output += "previous hash: " + cur_block.previous_hash + "\n"
            output += "hash: " + cur_block.hash + "\n"
            output += "\n"

            cur_block = cur_block.next

        return output

def test_driver_verify_chain(chain, name):
    if chain.verify_chain():
        print(f"{name} chain is valid")
    else:
        print(f"{name} chain is NOT valid")

# Test Cases

##########
# Test Case 1: Nominal
tc1_bc = Blockchain()
tc1_bc.add_block('a')
tc1_bc.add_block('b')
tc1_bc.add_block('c')
print('Test Case 1')
print(tc1_bc)
test_driver_verify_chain(tc1_bc, "TC1")
# Expected Output: Chain with nodes that have data 'a', 'b', 'c' (in that order) where, for all nodes, the value of
# previous hash for a node is equal to the hash value of the previous node.  As a result, the chain is valid.
print('----------')

# Test Case 2: Empty Data
tc2_bc = Blockchain()
tc2_bc.add_block('a')
tc2_bc.add_block('') # empty data
tc2_bc.add_block('') # empty data
print('Test Case 2')
print(tc2_bc)
test_driver_verify_chain(tc2_bc, "TC2")
# Expected Output: Chain with nodes that have data 'a', '' (empty string), '' (empty string) (in that order) where,
# for all nodes, the value of previous hash for a node is equal to the hash value of the previous node.
# As a result, the chain is valid.
print('----------')

# Test Case 3: Invalid First Block (modified data after the block was created)
tc3_bc = Blockchain()
tc3_bc.add_block('a')
tc3_bc.add_block('b')
tc3_bc.add_block('c')
tc3_bc.head.data = 'aa' # modifying data
print('Test Case 3')
print(tc3_bc)
test_driver_verify_chain(tc3_bc, "TC3")
# Expected Output: Chain with nodes that have data 'aa', 'b', 'c' (in that order) where the stored hash value
# for the node with data 'aa' does not align with the recalculated hash value for the node.
# As a result, the chain is NOT valid.
print('----------')

# Test Case 4: Invalid Non-First Block (modified data after the data was created)
tc4_bc = Blockchain()
tc4_bc.add_block('a')
tc4_bc.add_block('b')
tc4_bc.add_block('c')

cur_node = tc4_bc.head
while cur_node:
    if cur_node.data == 'b':
        break
    else:
        cur_node = cur_node.next
cur_node.data = 'bb' # modifying data
cur_node.hash = cur_node.calc_hash() # try to cover up the modified data

print('Test Case 4')
print(tc4_bc)
test_driver_verify_chain(tc4_bc, "TC4")
# Expected Output: Chain with nodes that have data 'a', 'bb', 'c' (in that order) where the previous hash value
# for the node with data 'c' does not align with the hash value for the node with data 'bb'.
# As a result, the chain is NOT valid.