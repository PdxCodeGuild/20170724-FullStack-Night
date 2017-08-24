# Lab 27: Practice Problems #3


## Problem 1

Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

```python
opposite(10, -1) → True
opposite(2, 3) → False
opposite(-1, -1) → False
```
## Problem 2

Write a function that returns True if a number within 10 of 100.

```python
near_100(50) → False
near_100(99) → True
near_100(105) → True
```


## Problem 3

Write a function that takes a string, and returns a list of strings, each missing a different character.

```python
missing_char('kitten') → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']
```


## Problem 4

Write a function that returns the number of occurances of 'hi' in a given string.

```python
count_hi('hihi') → 2
```

## Problem 5

Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

```python
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('catdogcatdog') → True
```

## Problem 6

Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

```python
eveneven([5, 6, 2]) → True
eveneven([5, 5, 2]) → False
```


## Problem 7

Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.

```python
nums = [[5,2,3],[4,5,1],[7,6,3]]
combine_all(nums) → [5,2,3,4,5,1,7,6,3]
```


## Problem 8

Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

```python
fibonacci(8) → [1, 1, 2, 3, 5, 8, 13, 21]
```





