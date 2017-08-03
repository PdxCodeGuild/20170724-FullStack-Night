# Lab 1: Mad Libs

Write a simple program that, when run, prompts the user for several inputs then
 prints a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) as the result.


## Concepts Covered

- input, print
- variables, assignment
- string concatenation

## Instructions

1. Search the interwebs for an example Mad Lib
2. Create a new file and save it as `madlib.py`
3. Ask the user for each word you'll put in your Mad Lib
4. Use `string concatenation` to put each word into the Mad Lib

## Example:

```
>>> Give me an antonym for 'data': nonmaterial
>>> Tell me an adjective: Bearded
>>> Give me a sciency buzzword: half-stack
>>> A type of animal (plural): parrots
>>> Some Sciency thing: warp drive
>>> Another sciency thing: Trilithium crystals
>>> Sciency adjective: biochemical
...
>>> Nonmaterial Scientist Job Description:
>>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
>>> Key responsibilities:
>>> - Extract patterns from non-material
>>> - Optimize warp drive
>>> - Transform trilithium crystals into biochemical material.
```

-------

## Version 2 (optional)

Add randomness! Use `random.choice`, to randomly choose from a list of adjectives, verbs, nouns, etc.

## Version 3 (optional)
Make the game repeatable: prompt for a list of words, print the story, then ask them if they'd like to do it again.

## Version 4 (optional)

Allow the user to enter multiple words at once, separated by commas. Use `split` to separate the whole string into a list of words.