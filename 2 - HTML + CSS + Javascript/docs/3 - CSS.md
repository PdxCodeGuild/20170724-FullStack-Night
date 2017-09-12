

# CSS

## Defining CSS

There are two ways to define CSS, the first is through 'inline styles' (a style attribute).

```
<div style="background-color:black">
    <div style="background-color:lightblue">blahblahblah</div>
    <div style="background-color:DarkOliveGreen">blahblahblahwaoekfawpoef</div>
    <div style="background-color:#FF8C00">blahblahblahwaoekfawpoef</div>
    <div style="background-color:rgb(255,140,0)">this is the same color as above</div>
</div>
```

Style attributes are separated via semi-colons.

```
<div style="color:blue;background-color:DarkOliveGreen">This is some ugly text</div>
```

Inline styles are fine when prototyping, but consider the following case.

```
<ol>
    <li style="color:red">Apple</li>
    <li style="color:red">Banananana</li>
    <li style="color:red">Pear</li>
</ol>
```

This can become tedious to update and make changes to, because we have to edit the same value in multiple places every time we want to make a change. Therefore, it's generally better to use a style tag, and it's generally better to put it in the page head.

```
<head>
    <style>
        li {
            color:red
        }
    </style>
</head>
<body>
    <ol>
        <li>Apple</li>
        <li>Banananana</li>
        <li>Pear</li>
    </ol>
</body>
```

A third way to define CSS is via an 'external style-sheet' or a separate file with the extension 'css'. You can then import it with a `link` tag. This is also generally done in the page head.

```
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```



## CSS Properties

- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference
- https://www.w3schools.com/cssref/





## CSS Selectors

- https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Simple_selectors
- https://www.w3schools.com/cssref/css_selectors.asp
- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors


### Tag Selector

Just put the tag name:
```
h1 {
    font-size:20px;
}

p {
    font-lize:12px;
}
```

### Class Selector

Put a `.` before the class name

```
<style>
    .error {
        color: red;
        border: 1px solid red;
    }
    .warning {
        color: yellow;
        border: 1px solid yellow;
    }
</style>
<div class="error">This is an error message</div>
<div class="warning">This is a warning</div>
```

### ID Selector

Put a `#` in front of the ID, this allows you to address a specific tag.

```
<style>
    #paragraph1 {
        font-size: 12px;
    }
    #paragraph2 {
        font-size: 10px;
    }
</style>
<p id="paragraph1">blahblahblah</p>
<p id="paragraph2">blahblahblah</p>
```


### Universal Selector

Using a `*` will select everything, it's generally better to apply a style to the `body` tag and let sub-tags pick it up.


## CSS Properties


`display: none`
