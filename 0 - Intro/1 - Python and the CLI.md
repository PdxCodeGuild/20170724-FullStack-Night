
# Python and the CLI

## Installing Python

### Anaconda

This installs many packages and tools.

https://www.continuum.io/downloads


### Python and Pip

`Pip` is the package manager for python. Always start by updating pip itself, `pip3 install --upgrade pip`, Then you can install packages by running commands such as `pip3 install jupyter`.


## Using the CLI

### Opening the CLI

In OS X, the default CLI is called `Terminal`, which you can find by typing `terminal` in search, or under `Finder -> Applications -> Utilities`.

In Windows, the default CLI is `cmd`, which you can find by typing `cmd` in search, or pressing `Windows+R`, typing `cmd`, and hitting `enter`. This will work for executing python things, but there's no color differentiation, and some commands like `ls` and `rm` won't work in `cmd`. A much better CLI is [Cmder](http://cmder.net/), which looks better and offers more control, plus, it comes with git! Another option for Windows is [Powershell](https://msdn.microsoft.com/en-us/powershell/scripting/setup/installing-windows-powershell).

In Linux, you can open a terminal with `Ctrl + Alt + T`.

### Common CLI Commands

- `pwd` displays the path of the current directory
- `ls` lists the contents of the current directory
- `cd <directoryname>` change directory
    - `cd ..` will bring you into the parent directory
    - `cd` alone will return you to your 'home' directory
- `mkdir <foldername>` create a new folder 
- `rmdir <foldername>` removes a folder
- `rm <filename>` removes a file
- `mv filename1 filename2` moves or renames a file
- `cp filename1 filename2` copies a file
- `ctrl+c` kill currently running process


## Running Python via the CLI


### Using the Python Interactive Interpreter

Open a terminal and type `python`, you should see a welcome message, and be left with `>>>`. Try typing in the following commands.

```
>>> 5 + 3
8
>>> 4*(5+1)+8
32
```

We can let names stand for values, like in algebra.

```
>>> x = 5
>>> x = x + 3
>>> x
8
```


### Executing Python Source Files

You can execute python code saved in a plain text file by typing `python filename`. Create a new file `temp.py` with the following contents:

```
x = 5
x = x + 3
print(x)
```

Execute this file by opening a terminal, and type `python temp.py`. You should see `8` as the output. Every time you edit the source file, you then run it by typing `python filename` again.