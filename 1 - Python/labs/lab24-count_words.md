# Lab 24: Count Words

Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal.


Find a book on [Project Gutenberg](http://www.gutenberg.org).
Download it as a UTF-8 text file.

1. Open the file.
2. Make everything lowercase, strip punctuation, split into a list of words.
3. Your dictionary will have words as `keys` and counts as `values`. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
4. Print the most frequent top 10 out with their counts.



## Version 2

Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

## Version 3 (optional)

Let the user enter a word, then show the words which most frequently follow it.