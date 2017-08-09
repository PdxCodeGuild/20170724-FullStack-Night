# Lab 17: Practice Problems 2





## Problem 1

Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.

```
>>> Enter a number (or 'done'): 5
>>> Enter a number (or 'done'): 34
>>> Enter a number (or 'done'): 515
>>> Enter a number (or 'done'): done
[5, 34, 515]
```


## Problem 2


```
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print_every_other(nums)
```
```
0, 2, 4, 6, 8
```

Print out every other element of a list, first using a while loop, then using a for loop.


## Problem 3

Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number

```
nums = [5, 6, 2, 3]
target = 7
find_pair(nums, target)
```
```
[5, 2]
```



## Problem 4

Get a string from the user, print out another string, doubling every letter.

```
>>> Enter some text: hello
hheelloo
```

# Problem 5

Write a function that merges two lists into a single list, where each element of the outlist list is another list containing two elements.

`merge([5,2,1], [6,8,2])` -> `[[5,6],[2,8],[1,2]]`