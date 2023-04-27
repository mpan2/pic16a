'''
PIC 16A Homework 2
Author: Michelle Pan
UID: 105623333
Discussion Section: 3B
Date: 04/23/2023
'''
def longestpath(d):
    def dfs(key, visited):
        if key not in d:
            return 0  # if key not in d, return 0 as base case

        if key in visited:
            return 0  # if key already visited, return 0 to avoid cycles

        visited.add(key)  # mark key as visited
        return 1 + dfs(d[key], visited)  # recursive call with updated visited set

    maxPath = 0  # initialize maxPath to 0

    for key in d:
        maxPath = max(maxPath, dfs(key, set()))  # update maxPath with longest path found so far

    return maxPath

# Test cases
d1 = {"a": "b", "b": "c"}
d2 = {"a": "b", "b": "c", "c": "d", "e": "a", "f": "a", "d": "b"}

print(longestpath(d1))  # Output: 2
print(longestpath(d2))  # Output: 5
