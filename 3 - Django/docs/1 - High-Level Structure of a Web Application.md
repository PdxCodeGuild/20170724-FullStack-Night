# 1 - High-Level Structure of a Web App

## What is a web application?

A web application is a site hosted on the web that offers significant functionality beyond simple, static pages. They often allow users to log in and save their work and are usually connected to a database of some kind. [Amazon](http://amazon.com), [LinkedIn](http://linkedin.com), and [Trello](http://trello.com) are all examples of web applications.

A web application has three big moving parts:

1. Database
1. Back-End
1. Front-End

## Database

This is the **persistent datastore**. Every other part of the app is _stateless_ and can't "remember" things. Around the database is a program that receives and responds to 'queries', which are requests to store or retrieve data. We'll be using SQL "Structured Query Language" databases, but we will use an ORM "Object-Relational Mapping" to interface with them and will not delve deeply (if at all) into SQL. Using an ORM, we can write simple statements in Python to interact with our database.

## Back-End

This is your **web server**. It serves dynamically generated web pages. When someone goes to `www.yourwebsite.com/show/ponies`, it will figure out what's on `/show/ponies`, maybe by talking to the database or other web sites, and return the content associated with it for display. This is the code you write in **Python**.
It contains your _business logic_. You will use a **web framework** that handles all of the input and output;
all you have to do is figure out how to generate output **content** for an input **path**.

## Front-End

This is the **HTML**, **CSS**, and **JavaScript** that your web server returns. The HTML is the actual structured content that your server wants to show the user. The CSS describes the presentation of the content. The JavaScript is code for the user's web browser to run to enable complex _interactions_ with the user.