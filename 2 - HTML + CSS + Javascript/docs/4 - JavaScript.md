
# 4 - JavaScript


## Variables

In JavaScript, we declare a variable by writing `var`. Unlike Python, JavaScript uses c-styled syntax: each statement is terminated with a semi-colon, white-space doesn't matter, and the bodies of objects, loops, and functions use curly-braces. Like Python, however, strings can use either single-quotes or double-quotes, and use escape sequences for newlines, tabs, and backslashes.

```JavaScript
var a = 5;
var b = 10.4;
var c = "hello!";
```

Use `//` for line-comments, `/* ... */` for block-comments.

JavaScript can be written inline, in a script tag, or in an external file.

```JavaScript
<button onclick="alert('Hello World!')">click me</button>

<script>
    alert("hello world!");
</script>

<script src="myscript.js"></script>
```

Getting output to the user can be done three ways. Using the console won't display the output to a user, but will display it in the developer tools. This also gives you a way to pick through an object, attribute by attribute, rather than looking at a messy string.

```
alert("Hello World!");
console.log("Hello World!");
```

In your browser, you can open the developer tools by pressing `F12`. This contains a real-time view of the DOM, selecting an element will let you view the CSS it uses. The Dev Tools also contain a JavaScript Console that'll let you see the output of the page's JavaScript and any exceptions that occur.

There's also `document.write(s)` which will replace all existing HTML on the page.

## Data Types

```JavaScript
var a = 5; // int
var b = 10.4; // float
var c = "hello!"; // string
var d = true; // boolean
var e = null; // null
var f = undefined; // undefined

var fruits = ["apple", "bananana", "pear"] // array

var person = {firstName:"John", lastName:"Doe", age:46}; // object
person.age += 1;
person.favorite_fruit = "orange";
```

To convert between types, use `parseInt`, `parseFloat` and `toString`.

```JavaScript
var x = parseInt('4');
var y = parseFloat('4.2');
var z = x.toString();
```

## Math


```JavaScript
Math.abs(-4) // 4
Math.sqrt(16) // 4.0
Math.min(5, 6) // 5
Math.max(5, 6) // 6
Math.floor(4.5) // 4
Math.ceil(4.5) // 5
Math.round(4.5) // 5
Math.random() // between 0 and 1, but not including 1
Math.pow(5, 2) // 25
Math.PI // 3.14
Math.sin(Math.PI/2) // 1.0
Math.cos(Math.PI/2) // 0.0
```

## Strings

https://www.w3schools.com/jsref/jsref_obj_string.asp

## Comparisons

```JavaScript
var x = 0;
console.log(x == 0); // true
console.log(x != 0); // false
console.log(x < 10); // true
console.log(x > 10); // false
console.log(x <= 10); // true
console.log(x >= 10); // false
console.log(x > -10 && x < 10); //true
console.log(x > -10 || x < 10); // true
```

## Conditionals

```
var temperature = 56;
if (x < 60)
{
    alert('cold');
}
elif (x < 80)
{
    alert('warm');
}
else
{
    alert('hot');
}
```


## Arrays and Loops

You can access an array's length with `fruits.length`, you can append an element like `fruits.push('dragonfruit');`. You can find more info [here](https://www.w3schools.com/jsref/jsref_obj_array.asp).

```JavaScript
var fruits = ["apple", "bananana", "pear"]
fruits.push('cherry');
for (var i=0; i<fruits.length; ++i) {
    console.log(fruits[i]);
}
console.log(fruits.indexOf('bananana')); // 1
```


## Functions

There are multiple ways to use functions in javascript. Below we're 'declaring a function'.

```JavaScript
function add(a, b) {
    return a + b;
}
console.log(add(5, 2));
```

You can also assign the function to a variable.

```JavaScript
var add = function(a, b) {
    return a + b;
}
console.log(add(5, 2))
```


## DOM Manipulation

Get an element by ID and add some style:
```JavaScript
<div id="demo_div"></div>
...
var demo_div = document.getElementById('demo_div');
demo_div.innerHTML = "Hello World!";
demo_div.style.fontSize = 24;
demo_div.name = "demo_div" // setting at attribute

.....

<div id="demo_div" style="font-size:24" name="demo_div">Hello World!</div>


```

Get the value from an input:
```JavaScript
<input id="user_input" type="text"/>
...
var text_field = document.getElementById('user_input');
var user_input = text_field.value;
```

Create a button, style it, and add it to a div
```Javascript
<div id="container_div"></div>
...
var btn = document.createElement("button");
btn.style.backgroundColor = "lightblue";
btn.style.border = "1px solid white";

var container_div = document.getElementById('container_div')
container_div.appendChild(btn);
```

https://www.w3schools.com/js/js_htmldom_document.asp