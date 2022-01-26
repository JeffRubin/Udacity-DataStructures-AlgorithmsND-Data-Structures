class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += "None"
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    d1 = dict_from_linked_list(llist_1)
    d2 = dict_from_linked_list(llist_2)

    d1.update(d2) # keys are unique so there will be no duplicates

    union_ll = link_list_from_dict(d1)

    return union_ll

def intersection(llist_1, llist_2):
    d1 = dict_from_linked_list(llist_1)
    d2 = dict_from_linked_list(llist_2)

    intersection_dict = dict()
    for e in d1:
        if e in d2:
            intersection_dict[e] = e # keys are unique so there will be no duplicates

    intersection_ll = link_list_from_dict(intersection_dict)

    return intersection_ll

def dict_from_linked_list(llist):
    output = dict()

    cur_node = llist.head
    while cur_node:
        output[cur_node.value] = cur_node.value # key is all that reall matters
        cur_node = cur_node.next

    return output

def link_list_from_dict(dict):
    ll = LinkedList()

    if dict is not None:
        for e in dict:
            ll.append(e)

    return ll

# Test Cases

##########
# Test Case 1: Partial Intersection (With Duplicates)
linked_list_tc1_1 = LinkedList()
linked_list_tc1_2 = LinkedList()

element_tc1_1 = [3,2,4,35,6,65,6,4,3,21]
element_tc1_2 = [6,32,4,9,6,1,11,21,1]

for i in element_tc1_1:
    linked_list_tc1_1.append(i)

for i in element_tc1_2:
    linked_list_tc1_2.append(i)

print('Test Case 1')
print (union(linked_list_tc1_1,linked_list_tc1_2))
# Expected Output: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> None
print (intersection(linked_list_tc1_1,linked_list_tc1_2))
# Expected Output: 4 -> 6 -> 21 -> None
print('----------')

# Test Case 2: No Intersection (With Duplicates)
linked_list_tc2_1 = LinkedList()
linked_list_tc2_2 = LinkedList()

element_tc2_1 = [3,2,4,35,6,65,6,4,3,23]
element_tc2_2 = [1,7,8,9,11,21,1]

for i in element_tc2_1:
    linked_list_tc2_1.append(i)

for i in element_tc2_2:
    linked_list_tc2_2.append(i)

print('Test Case 2')
print (union(linked_list_tc2_1,linked_list_tc2_2))
# Expected Output: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> None
print (intersection(linked_list_tc2_1,linked_list_tc2_2))
# Expected Output: None
print('----------')

# Test Case 3: Complete Intersection (With Duplicates)
linked_list_tc3_1 = LinkedList()
linked_list_tc3_2 = LinkedList()

element_tc3_1 = [3,2,4,35,6,65,6,4,3,23]
element_tc3_2 = [3,2,4,35,6,65,6,4,3,23]

for i in element_tc3_1:
    linked_list_tc3_1.append(i)

for i in element_tc3_2:
    linked_list_tc3_2.append(i)

print('Test Case 3')
print (union(linked_list_tc3_1,linked_list_tc3_2))
# Expected Output: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> None
print (intersection(linked_list_tc3_1,linked_list_tc3_2))
# Expected Output: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> None
print('----------')

# Test Case 4: One Empty Linked List Input
linked_list_tc4_1 = LinkedList()
linked_list_tc4_2 = LinkedList()

element_tc4_1 = [3,2,4,35,6,65,6,4,3,23]

for i in element_tc4_1:
    linked_list_tc4_1.append(i)

print('Test Case 4')
print (union(linked_list_tc4_1,linked_list_tc4_2))
# Expected Output: 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> None
print (intersection(linked_list_tc4_1,linked_list_tc4_2))
# Expected Output: None
print('----------')

# Test Case 5: Two Empty Linked List Inputs
linked_list_tc5_1 = LinkedList()
linked_list_tc5_2 = LinkedList()

print('Test Case 5')
print (union(linked_list_tc5_1,linked_list_tc5_2))
# Expected Output: None
print (intersection(linked_list_tc5_1,linked_list_tc5_2))
# Expected Output: None
print('----------')
