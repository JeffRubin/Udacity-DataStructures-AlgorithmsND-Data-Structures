# Problem 2: File Recursion

## Overview
Used recursion to walk through the file structure.  Using recursion resulted in very brief code.

## Time Complexity: O(n)
O(n) where n is the number of directories under the specified path since have to scan all these directories to look
for the specified suffix.  Assuming k steps per directory (i.e. search through files in the directory, identify
other directories, add to output) results in O(kn) which is linear assuming k and n are not close to being equal.

## Space Complexity: O(n)
O(n) where n in the depth of the call stack at the deepest recursion level
(deepest directory under the specified path) since this is where the most memory will be in use
