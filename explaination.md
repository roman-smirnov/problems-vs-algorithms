# Problems Vs Algorithms Project

## Square Root
Our algorithm utiziles binary search between numbers whose squared value is smaller than the input number, and those larger than the input.
### Time Complexity
The wost case time complexity of our algorithm is O(log(n)) (the time complexity of binary search), where n is equal to the integer given as input.
### Space complexity
Our algorithm doesn't scale its storage requirements with input size, using only a few fixed variables, therefore the space complexity is O(1).

## Search in a Rotated Sorted Array
We divide the array into 2 sorted subarrays and use binary search to find the requested value.  
### Time Complexity
Our algorithm utilizes several applications of binary search, therefore the overall time complexity if O(log(n))
### Space Complexity
0The space complexity is as large as the input array, hence its O(n) at the worst case

## Rearrange Array Digits
Our algorithm makes use of a min-heap data structure to extract the lowest digit and iteratively construct the two output numbers.
### Time Complexity
The worst case time complexity is dictated by our utilization of the mean, hence it's O(nlogn)
### Space Complexity Complexity
Our algorithm stores all the digits required to construct both numbers. Thus, the space complexity is O(n). 

## Dutch National Flag
Our algorithm sorts the trinary array in a single transversal by maintaining, and swapping elements to, 3 separte reserved areas during the single pass.
### Time Complexity
Our algorithm performs a single pass over the input array, plus a number of swaps which is at worst the size of the input.
Therefore, the overall worst case runtime complexity of our algorithm is O(n).
### Space Complexity
The algorithm performs the sort in-place, hence its space complexity is O(n).

## Autocomplete with Tries
We store the characters in the trie data structure and perform search operation on it
### Time Complexity
All operations on the trie are done in O(n) time
### Space Complexity
The trie, and therefore the overall, space complexity is O(n)


## Max and Min in a Unsorted Array
We traverse the list and simultaneously maintain the current argmax  and argmin of the array
### Time Complexity
We perform a single pass over the array, hence the runtime complexity is O(n) 
### Space Complexity
The space complexity is O(n) since we do not store anything beyond the array itself and a few extra constant variables/


## Http Router
Our path routing algorithm breaks down a path to its inidiviual parts and utilizes a triep data structure for storage and search. 
### Time Complexity
Each individual part of our algorithm (split_path(), trie find(), etc) have O(n)  time complexity, where n is the number of parts in the input path.
Therefore, the overall worst case time complexity is O(n).
### Space Complexity
The worst case space complexity is O(n), where n is the number of parts in the path, due to our use of a trie to store the individual parts.

