# Problem 4: Archive Directory

## Overview
Used recursion to walk through the groups.  Using recursion resulted in very brief code.
Also, added a simple cache to track which groups have already been checked for users to prevent checking the
same group multiple times and to avoid infinite group loops where groups either contain themselves
or groups contain one another.

## Time Complexity: O(n)
O(n) where n is the total number of usernames under the group being searched for containment (including within subgroups).
Have to check all these names in the case that the specified username is not a member of the group being searched for
containment.

## Space Complexity: O(n)
- O(n) where n in the depth of the call stack at the deepest recursion level
(deepest group under the specified group).
- The cache of groups that have already been checked will also be O(n) at its maximum size where n is the number of unique
groups under the specified group in the case that the specified user is not in any group (so have to search all groups).
- n are different between these cases but the complexity is linear for both.