
# Regular Expressions (regex)

Regular expressions are a way to match patterns in strings. They can be used to validate a phone number or address in an input field on a website, they can be used to find the occurances of a phrase in a block of text, etc.

You can find out more about regular expressions [here](https://docs.python.org/3.6/howto/regex.html#regex-howto) and [here](https://docs.python.org/3.6/library/re.html#re-syntax).


- `[]` define a character class
- `^` within a character class, matches everything BUT what follows

- `$` matches the end of a string, or just before the next newline
- `*` matches 0 or more occurances
- `+` matches 1 or more occurances
- `?` matches 0 or 1 occurance

- `.` matches any character except a newline
- `\d` matches any digit character (0-9)
- `\s` matches any whitespace character (space, \t, or \n)
- `\w` matches any word character (A-Z, a-z, 0-9, and _)