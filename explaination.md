# Problems Vs Algorithms Project

## Http Router
Our path routing algorithm breaks down a path to its inidiviual parts and utilizes a triep data structure for storage and search. 
### Time Complexity
Each individual part of our algorithm (split_path(), trie find(), etc) have O(n)  time complexity, where n is the number of parts in the input path.
Therefore, the overall worst case time complexity is O(n).
### Space Complexity
The worst case space complexity is O(n), where n is the number of parts in the path, due to our use of a trie to store the individual parts.

