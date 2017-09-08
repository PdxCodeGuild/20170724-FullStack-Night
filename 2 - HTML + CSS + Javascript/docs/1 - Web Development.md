
# Web Development

## List of Terms


URL: Uniform Resource Locator, aka a web address. For example, `http://www.example.com/index.html`, `http` is the protocol, `www.example.com` is the hostname, and `index.html` is the file. [(more info)](https://en.wikipedia.org/wiki/URL#Syntax)

IP Address: a numerical address assigned to each device that's connected to a network. A dynamic IP can change over time, and may be different every time the device is connected to the network. Most users have dynamic IPs. A static IP is constant, and is used by servers hosting websites. An IP address may also have a port specified. An IPv4 address consists of 4 numbers, each in the range from 0 to 255 (the max value of 1 byte). IPv6 greatly expanded the number of available IP addresses.

DNS: Domain Name Server, a server that associates IP addresses and hostnames. When you type an address 'www.google.com' into your address bar and hit enter, your browser looks up the IP address for that hostname by querying the DNS. Then your browser executes a GET on the IP to get the web page.


Client-Server Model: the standard architecture of the web, allows centralization of information in servers which many clients can access simultaneously, as opposed to the peer-to-peer model.

TCP/IP: the fundamental communications protocol (a standardized way of sending and receiving data) for the web.

Packet: A small segment of data which contains headers indicating the sender and receiver.

HTTP: Hypertext Transfer Protocol, rests on top of TCP/IP.

FTP: File Trasfer Protocol, also rests on top of TCP/IP.

HTML: Hypertext Markeup Language, a way of formating elements on a web page.

CSS: Cascading Style Sheets, a way to add color, style, and animation to HTML.

Javascript: a scripting language with superficially similar syntax to Java, may be used for both the front-end and back-end.

Database: a collection of data, stored and retrieved through queries.

Front-End: code that runs on the client (in your browser), which usually consists of Javascript, HTML, and CSS.

Back-End: code that runs on the server, deals with data processing, files, and databases and can involve a variety of different languages.

## Request-Response Cycle

### Common HTTP Requests

GET: retrieve data

POST: create data

PUT: update data

DELETE: delete data

### HTTP Response Types

1XX Informational responses

2XX Success

3XX Redirection

4XX Client errors

5xx Server errors

### Common HTTP Responses

200 OK

301 Moved Permanently

403 Forbidden

404 Not Found

500 Internal Server Error


### Common Ports

20/21 FTP

22 SSH (Secure Shell)

25 SMTP (Simple Mail Transfer Protocol)

53 DNS

80 HTTP

