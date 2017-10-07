
# 2 - Django Overview

Django is a popular [web application framework](https://www.fullstackpython.com/web-frameworks.html) built in Python. It was created in 2003 by [Simon Willison](https://en.wikipedia.org/wiki/Simon_Willison) and [Adrian Holovaty](https://en.wikipedia.org/wiki/Adrian_Holovaty), the latter of whom plays gypsy-jazz guitar and is a big fan of [Django Reinhardt](https://www.youtube.com/watch?v=PQhTpgicdx4) (video).

More specifically, Django is a Python library that includes tools for making a dynamic web server. It gives you web framework to handle the piping involved in a web server and an ORM to talk to a database easily.

## What is a web application framework?

A **web application framework** is a library that does all of the piping for writing a web server for you. The most basic operation is to match URLs with code that should run and produce a response. Web application frameworks make it easier to write web applications by providing simple ways to build common functionality including the following:

- Authentication
- Routes
- Models
- Views/templates
- Plugin architecture

You can write a function for each URL in your site, called a **view**. Then link them to the actual URL pattern, called a **route**. Then fill in the function with whatever code is necessary to produce the HTML content. It could talk to a DB, another web server, crunch lots of numbers, just read a file, etc.

Django also gives you an "admin interface" to your database that auto generates pages that let you debug and inspect the values in there.

## Django isn't a CMS

Django does not directly fill the same role as WordPress or Drupal.
Both of those are **content management systems** or **CMS**.

They give you a pre-made interface to upload content and have it be displayed on a web page.
They are opinionated about the structure of content you can use, although they are extendable through plugins that you can write.
You can those CMSs do all the things you do here, but you'll often be working _against_ it's options rather than working with the basic tools of Django.

## What does Django do for me?

The Django framework follows a "batteries included" philosophy. What this means is that the functions common to web applications are built-in to the framework rather than requiring external code (usually called 'plugins').

Some of the features of Django include the following:

- a lightweight and standalone web server for development and testing
- a form serialization and validation system that can translate between HTML forms and values suitable for storage in the database
- a template system that utilizes the concept of inheritance borrowed from object-oriented programming
- a caching framework that can use any of several cache methods
support for middleware classes that can intervene at various stages of request processing and carry out custom functions
- an internal dispatcher system that allows components of an application to communicate events to each other via pre-defined signals (often called “hooks” in other frameworks)
- an internationalization system, including translations of Django's own components into a variety of languages
- a serialization system that can produce and read XML and/or JSON representations of Django model instances
- a system for extending the capabilities of the template engine
an interface to Python's built in unit test framework
- an extensible authentication system
- the dynamic administrative interface
- tools for generating RSS and Atom syndication feeds
- a sites framework that allows one Django installation to run multiple websites, each with their own content and applications
tools for generating Google Sitemaps
- built-in mitigation for cross-site request forgery, cross-site scripting, SQL injection, password cracking and other typical web attacks, most of them turned on by default