import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    output = []

    try:
        dir_contents = os.listdir(path)
    except FileNotFoundError:
        print(f"Invalid path: {path}")
        return output

    for item in dir_contents:
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            if item_path.endswith(suffix): # otherwise it's not the kind of file being search for so pass on it
                # compatability for Unix and Windows from: https://stackoverflow.com/questions/13162372/using-absolute-unix-paths-in-windows-with-python
                output.append(os.path.abspath(os.path.expanduser(item_path)))
        elif os.path.isdir(item_path):
            next_level = find_files(suffix, item_path)
            output.extend(next_level)
        else:
            raise ValueError('Input is not a file or a directory')

    return output

# Test Cases

##########
# Test Case 1: Nominal Find .c Files From Top Of The File Structure
print('Test Case 1')
print(find_files('.c', './testdir'))
# Expected Output: [./testdir/subdir1/a.c, ./testdir/subdir3/subsubdir1/b.c, ./testdir/subdir5/a.c, , ./testdir/t1.c]
print('----------')

# Test Case 2:  Nominal Find .c Files From Within The File Structure
print('Test Case 2')
print(find_files('.c', './testdir/subdir3'))
# Expected Output: [./testdir/subdir3/subsubdir1/b.c]
print('----------')

# Test Case 3: Invalid Path
print('Test Case 3')
print(find_files('.c', './null'))
# Expected Output: [] with an message indicating that the specified path is not valid
print('----------')

# Test Case 4: No Suffix Matches
print('Test Case 4')
print(find_files('.d', './testdir'))
# Expected Output: []
print('----------')

# Test Case 5: Suffix Matches Everything
print('Test Case 5')
print(find_files('', './testdir'))
print('----------')
# Expected Output: [./testdir/subdir1/a.c, ./testdir/subdir1/a.h, ./testdir/subdir2/.gitkeep,
# ./testdir/subdir3/subsubdir1/b.c, ./testdir/subdir3/subsubdir1/b.h, ./testdir/subdir4/.gitkeep,
# ./testdir/subdir5/a.c, ./testdir/subdir5/a.h, ./testdir/t1.c, ./testdir/t1.h]

# Test Case 6: Empty Path
print('Test Case 6')
print(find_files('.c', './emptydir'))
# Expected Output: []
