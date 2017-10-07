

# Philosophy of Programming


## A Brief History of Computation





## What is a Program?


A `program` is a series of instructions given to a computer which perform operations on data, transforming input into output. Programmers write these instructions into text files, then run in either through a `compiler` or `interpreter`.

A `compiler` is a program that translates source code into `machine code`, which can then be executed directly by the CPU. Machine code is extremely terse, each statement represents a single discrete operation to be performed by the CPU. They consist of things such as 'move these 4 bytes from memory to a register', and 'add the two numbers from these two registers, and store the result in a third register'. An executable file (.exe) is nothing more than a series of instructions in machine code. When executed, the Operating System loads the machine code into memory and begins executing it, statement by statement.

Obviously writing large and complex programs directly in assembly would be extremely difficult to write and maintain and understand. So we invented compilers and 'higher-level languages'. A single statement in a high-level language corresponds to multiple statements to many statements in assembly. The syntax or grammar of the language is a standard that both programmers and the compiler adhere to.

An `interpreter` is a program that executes one statement at a time, executing machine code on your behalf. 

Higher-level languages gave rise to multiple programming paradigms, like `functional programming` and `object-oriented programming`.


## Fields of programming:
- Web Development
    - Front-End: HTML, CSS, Javascript
    - Back-End: Database, IT
- Networking: TCP/IP, UDP
- Cryptography, Security
- Computer Graphics, Video
- Game Development
- Desktop Applications
- Mobile Applications: Android, iOS, Windows Mobile
- Embedded Systems
- Data Science, 'Big Data', Artificial Intelligence


## Compilation vs Interpretation

Obviously writing a large program in assembly will quickly become tedious.

Compilation allows us humans to meet the computer 'half-way'.


Assembly is the 'lowest-level language', C is a low-level language, C++ in slightly higher, C#, Python, and Java are high-level languages. Low-level languages are more difficult to master, more susceptible to bugs, and slower to develop, but can be more efficient if implemented properly. But the responsibility is placed on the programmer to carefully design the high-level order of their program, or else it'll quickly become unmanagable.



## Language vs Framework

A framework or library, is a collection of pre-built code, usually written in the language in which you're using it.




## Open vs Closed Source





## Varieties of Programming Languages






### Imperative vs Declarative
	imperative - step by step
	declarative - define relationships
	
	x = 5
	y = 2*x
	x = 10
	print(y)

In a declarative language, the second line defines a relationship, not an operation to be performed.





procedural vs object-oriented
	procedural - cascade of execution
	object-oriented - relationships, interfaces
		group data and functions together



strong vs weak typing
    truthiness
    



static vs dynamic typing







#### Programming Languages

| type | language |
| ----|-----|
| Imperative | C, C++, C#, Java, Python |
| Functional | Haskell, Lisp & Scheme, Scala |
| Declarative | Prolog |
| Query | SQL, GraphQL, OCL, LINQ |


#### Non-Programming Languages

| type | language |
| ----|-----|
| Data Formatting|  JSON, XML|
| Markup | HTML, MD|
| Style | CSS|


### Self-Documenting Code

