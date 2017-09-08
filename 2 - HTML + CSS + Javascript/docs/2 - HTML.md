
# HTML

For a complete list of tags, look here: https://developer.mozilla.org/en-US/docs/Web/HTML/Element

## The Page Template

Below is the fundamental template for all HTML pages, the highest level tag is `html`. The `head` tag contains the metadata for the page. It can also contain a `title` tag, which determines the text that's displayed at the top of the browser window or on a tab. The `body` tag contains what's actually displayed to the user.
```
<html>
    <head>
        <title>This is an example page</title>
    </head>
    <body></body>
</html>
```
Tags can contain attributes, below is the anatomy of an html tag:
```
<tagname attribute="value"></tagname>
```


## Header Tags

The header (`h1`, `h2`, etc) let us define titles.
```
<h1>This is ordinarily used for the title</h1>
<h2>This is a chapter title</h2>
<h3>This is a sub-chapter title</h3>
<h4>and so on...</h4>
<h5>and so on...</h5>
```

## Paragraph Tags

The paragraph `p` tag lets us define paragraphs

```
<h3>Chapter 1: Lorem Ipsum</h3>
<p>Lorem ipsum dolor sit amet, consectetur...</p>
<p>Suspendisse elementum enim sed consectetur...</p>
<p>Donec at ligula hendrerit....</p>
```

## Lines and Breaks

The two tags `<hr/>` and `<br/>` are used without closing tags, and represent a broad horizontal line and line break respectively.

## Anchor Tags

The anchor tag `a` lets us create links.
```
<a href="http://www.google.com">click this</a>
```


## Image Tags

An `<img>` tag lets us display an image.
```
<img src="http://www.ackermanplumbing.com/ackermanplumbingserviceslogo.png" alt="Ackerman Plumbing" width="50" height="50"></img>
```


## Quotes and Block-Quotes

```
<q>this is a quote</q>

<blockquote>This is a blockquote. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam consectetur nisi nec orci maximus, at facilisis lorem dignissim. Fusce vitae orci pharetra, facilisis dui ut, ullamcorper ex.</blockquote>
```

## Division Tags

```
<div>This is a generic divider</div>
```


## Tables

Table are defined first by row, then by column.

```
<table>
    <tr>
        <td>A</td>
        <td>B</td>
    </tr>
    <tr>
        <td>C</td>
        <td>D</td>
    </tr>
    <tr>
        <td>E</td>
        <td>F</td>
    </tr>
</table>
```

Tables can also contain a top row of `th` 'table head' tags:


```
<table>
 <tr>
   <th>Month</th>
   <th>Savings</th>
 </tr>
 <tr>
   <td>January</td>
   <td>$100</td>
 </tr>
</table>
```

## Pre-formatted Text

The `<pre>` tag allows pre-formatted text, and preserves spaces and line breaks.

```
<pre>
  My Bonnie lies over the ocean.

  My Bonnie lies over the sea.

  My Bonnie lies over the ocean.

  Oh, bring back my Bonnie to me.
</pre>
```

## Tool-Tips

The `title` attributes allows us to add a tooltip on any element.
```
<p title='this is useful for describing things'>hover over me</p>
```


## Input and Select

`input` tags allow for user-input. A `select` tag defines a drop-down box.

```
<input type="text"></input>
<input type="date"></input>
<input type="color"></input>
<input type="password"></input>
<input type="radio"></input>
<input type="checkbox"></input>
<select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="mercedes">Mercedes</option>
  <option value="audi">Audi</option>
</select>
```

If radio buttons are given the same `name` attribute, they'll only allow one option to be selected at a time.

```
<input type="radio" name="gender" value="male"> Male<br>
<input type="radio" name="gender" value="female"> Female<br>
<input type="radio" name="gender" value="other"> Other
```


## Buttons

`<button>this is a button</button>`


## Ordered and Unordered Lists

Unordered lists are shown with bullet points, ordered lists are shown with numbers.

```

<ul>
    <li>Apple</li>
    <li>Banananana</li>
    <li>Pear</li>
</ul>


<ol>
    <li>Apple</li>
    <li>Banananana</li>
    <li>Pear</li>
</ol>
```



