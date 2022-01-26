class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        # added this duplicate check to prevent duplicate users in the same group;
        # this does not affect the logic for checking if a user is in a group but makes the list of users cleaner
        if user not in self.users:
            self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if type(group) != Group:
        raise ValueError("Must provide a valid Group object for the group argument")

    # a sort of cache to prvent checking groups that have already been checked (e.g. duplicates)
    # and in particular to address circular group references
    groups_already_checked = dict()
    return is_user_in_group_recur(user, group, groups_already_checked)


def is_user_in_group_recur(user, group, groups_already_checked):
    if user in group.get_users():
        return True
    else:
        groups_already_checked[group.get_name()] = True

        for g in group.get_groups():
            if g.get_name() in groups_already_checked: # do not need to check this group since it was already checked
                continue
            user_in_group = is_user_in_group_recur(user, g, groups_already_checked)
            if user_in_group:
                return True

    return False

def test_driver(user, group):
    if is_user_in_group(user, group):
        print(f"{user} is part of the {group.name} group")
    else:
        print(f"{user} is NOT part of the {group.name} group")

# Test Cases
# Each test case is meant to be standalone so tcx only uses variables for tcx where x is the test number

##########
# Test Case 1: Nominal
tc1_parent = Group("tc1_parent")
tc1_child = Group("tc1_child")
tc1_sub_child = Group("tc1_sub_child")

tc1_sub_child_user = "tc1_sub_child_user"
tc1_sub_child.add_user(tc1_sub_child_user)
tc1_sub_child_orphan = "tc1_sub_child_orphan" # not part of any group

tc1_child.add_group(tc1_sub_child)
tc1_parent.add_group(tc1_child)

print('Test Case 1')
test_driver(tc1_sub_child_user, tc1_sub_child)
# Expected Output: TRUE
test_driver(tc1_sub_child_user, tc1_child)
# Expected Output: TRUE
test_driver(tc1_sub_child_user, tc1_parent)
# Expected Output: TRUE

test_driver(tc1_sub_child_orphan, tc1_sub_child)
# Expected Output: FALSE
test_driver(tc1_sub_child_orphan, tc1_child)
# Expected Output: FALSE
test_driver(tc1_sub_child_orphan, tc1_parent)
# Expected Output: FALSE
print('----------')

# Test Case 2: Empty String User (allowed but not ideal)
tc2_parent = Group("tc2_parent")
tc2_child = Group("tc2_child")
tc2_sub_child = Group("tc2_sub_child")

tc2_sub_child_user = ""
tc2_sub_child.add_user(tc2_sub_child_user)

tc2_child.add_group(tc2_sub_child)
tc2_parent.add_group(tc2_child)

print('Test Case 2')
# Note that these will print '' (empty string) for test output since that's the user name
test_driver(tc2_sub_child_user, tc2_sub_child)
# Expected Output: TRUE
test_driver(tc2_sub_child_user, tc2_child)
# Expected Output: TRUE
test_driver(tc2_sub_child_user, tc2_parent)
# Expected Output: TRUE
print('----------')

# Test Case 3: Group contains itself as a group (circular group)
tc3_parent = Group("tc3_parent")
tc3_child = Group("tc3_child")
tc3_sub_child = Group("tc3_sub_child")

tc3_sub_child_user = "tc3_sub_child_user"
tc3_sub_child.add_user(tc3_sub_child_user)
tc3_sub_child_orphan = "tc3_sub_child_orphan" # not part of any group

tc3_sub_child.add_group(tc3_sub_child) # group adds itself
tc3_child.add_group(tc3_sub_child)
tc3_child.add_group(tc3_child) # group adds itself
tc3_parent.add_group(tc3_child)
tc3_parent.add_group(tc3_parent) # group adds itself

print('Test Case 3')
test_driver(tc3_sub_child_user, tc3_sub_child)
# Expected Output: TRUE
test_driver(tc3_sub_child_user, tc3_child)
# Expected Output: TRUE
test_driver(tc3_sub_child_user, tc3_parent)
# Expected Output: TRUE

test_driver(tc3_sub_child_orphan, tc3_sub_child)
# Expected Output: FALSE
test_driver(tc3_sub_child_orphan, tc3_child)
# Expected Output: FALSE
test_driver(tc3_sub_child_orphan, tc3_parent)
# Expected Output: FALSE
print('----------')

# Test Case 4: Group A contains a Group B that itself contains Group A (circular groups)
tc4_parent = Group("tc4_parent")
tc4_child = Group("tc4_child")
tc4_sub_child = Group("tc4_sub_child")

tc4_sub_child_user = "tc4_sub_child_user"
tc4_sub_child.add_user(tc4_sub_child_user)
tc4_sub_child_orphan = "tc4_sub_child_orphan" # not part of any group

tc4_sub_child.add_group(tc4_child) # add group that will contain this group
tc4_child.add_group(tc4_sub_child)
tc4_child.add_group(tc4_parent)  # add group that will contain this group
tc4_parent.add_group(tc4_child)

print('Test Case 4')
test_driver(tc4_sub_child_user, tc4_sub_child)
# Expected Output: TRUE
test_driver(tc4_sub_child_user, tc4_child)
# Expected Output: TRUE
test_driver(tc4_sub_child_user, tc4_parent)
# Expected Output: TRUE

test_driver(tc4_sub_child_orphan, tc4_sub_child)
# Expected Output: FALSE
test_driver(tc4_sub_child_orphan, tc4_child)
# Expected Output: FALSE
test_driver(tc4_sub_child_orphan, tc4_parent)
# Expected Output: FALSE
print('----------')

# Test Case 5: Duplicate users in different groups that contain one another
tc5_parent = Group("tc5_parent")
tc5_child = Group("tc5_child")
tc5_sub_child = Group("tc5_sub_child")

tc5_sub_child_user = "tc5_sub_child_user"
tc5_sub_child.add_user(tc5_sub_child_user)
tc5_child_user = tc5_sub_child_user # same user which will be present in in different groups that contain one another
tc5_child.add_user(tc5_child_user)

tc5_child.add_group(tc5_sub_child)
tc5_parent.add_group(tc5_child)

print('Test Case 5')
test_driver(tc5_sub_child_user, tc5_sub_child)
# Expected Output: TRUE
test_driver(tc5_sub_child_user, tc5_child)
# Expected Output: TRUE
test_driver(tc5_sub_child_user, tc5_parent)
# Expected Output: TRUE

# Note that these will also print 'tc5_sub_child_user' for test output since the user name is the same
test_driver(tc5_child_user, tc5_sub_child)
# Expected Output: TRUE
test_driver(tc5_child_user, tc5_child)
# Expected Output: TRUE
test_driver(tc5_child_user, tc5_parent)
# Expected Output: TRUE
print('----------')
