
# APIs and AJAX

API stands for "application programming interface", it's a standardized way to send and receive data from a web service via HTTP requests (GET, POST, PUT, DELETE). There are many free and open APIs available on the internet that can provide many different data services. For example, try executing this url in your browser `http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en`. This is an api for random inspiration quotes. Note the query parameters, which specify a key, format, and language. When you enter it in your browser, you execute an HTTP GET request. You can do the same thing from JavaScript, then process the result and control how it's displayed to the user.

AJAX stands for "asynchronous javascript and XML", and allows you to execute HTTP requests from JavaScript. Here's how to execute an AJAX request in native JavaScript. Remember status 200 means 'success'.

```
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
        console.log(this.responseText);
    }
};
xhttp.open("GET", 'https://api.iify.org/?format=json');
xhttp.send();
```

The possible values for `readyState` are shown below, you can find more info [here](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState)
- 0 UNSENT: the request has not yet been sent
- 1 OPENED: the connection has been opened
- 2 HEADERS_RECEIVED: the response headers have been received
- 3 LOADING: the response body is loading
- 4 DONE: the request has been completed


It's a little more succinct in jQuery:

```
$.ajax({
    method: "GET",
    url: 'https://api.iify.org/?format=json'
}).done(function(data) {
    console.log(data);
}).fail(function() {
    alert("error");
});
```
