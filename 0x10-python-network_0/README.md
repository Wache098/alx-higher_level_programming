What a URL is
A URL (Uniform Resource Locator) is the address used to access resources on the internet. It specifies the location of a resource and the mechanism to retrieve it. For example, https://www.example.com/index.html is a URL.

What HTTP is
HTTP (Hypertext Transfer Protocol) is the protocol used for transferring hypertext requests and information on the internet. It is the foundation of any data exchange on the Web and it is a protocol used for transmitting hypertext via a network.

How to Read a URL
A URL typically has the following structure:

bash
Copy code
scheme://username:password@host:port/path?query#fragment
For example, in the URL https://www.example.com:8080/path/to/page?name=ferret#nose:

Scheme: https
Host: www.example.com
Port: 8080 (optional, default ports are 80 for HTTP and 443 for HTTPS)
Path: /path/to/page
Query string: ?name=ferret
Fragment: #nose
The Scheme for an HTTP URL
The scheme specifies the protocol to be used to access the resource. For HTTP URLs, the scheme can be either http or https:

http stands for Hypertext Transfer Protocol.
https stands for Hypertext Transfer Protocol Secure, which is HTTP with encryption (SSL/TLS).
What a Domain Name is
A domain name is a human-readable address used to identify a website on the internet, such as example.com. It maps to an IP address that the browser uses to locate the web server.

What a Sub-domain is
A sub-domain is a prefix to the domain name, used to organize and navigate to different sections of a website. For example, in blog.example.com, blog is the sub-domain.

How to Define a Port Number in a URL
A port number specifies the communication endpoint for the protocol. It is defined in a URL after the host and preceded by a colon. For example, in http://www.example.com:8080, 8080 is the port number.

What a Query String is
A query string is a part of a URL that assigns values to specified parameters. It follows the ? character in the URL. For example, in http://www.example.com?name=ferret&color=purple, name=ferret&color=purple is the query string.

What an HTTP Request is
An HTTP request is a message sent by a client to a server asking for a resource. It consists of:

A request line (e.g., GET /index.html HTTP/1.1)
Headers (e.g., Host: www.example.com)
An optional body (used in POST, PUT requests)
What an HTTP Response is
An HTTP response is a message sent by the server to the client in response to an HTTP request. It consists of:

A status line (e.g., HTTP/1.1 200 OK)
Headers (e.g., Content-Type: text/html)
An optional body (the requested resource or data)
What HTTP Headers are
HTTP headers are key-value pairs in both HTTP requests and responses that convey additional information. For example, Content-Type: application/json tells the client that the response body contains JSON data.

What the HTTP Message Body is
The HTTP message body is the part of the request or response that contains the actual data being transmitted. For example, in a POST request, the body might contain form data or JSON.

What an HTTP Request Method is
An HTTP request method indicates the desired action to be performed on the resource. Common methods include:

GET: Retrieve data
POST: Submit data
PUT: Update data
DELETE: Delete data
What an HTTP Response Status Code is
An HTTP response status code indicates the result of the HTTP request. Common status codes include:

200 OK: The request was successful.
404 Not Found: The requested resource was not found.
500 Internal Server Error: The server encountered an error.
What an HTTP Cookie is
An HTTP cookie is a small piece of data sent from a website and stored on the user's computer by the web browser. Cookies are used for state management (e.g., session management, user preferences).

How to Make a Request with cURL
cURL is a command-line tool for making HTTP requests. For example, to make a GET request to https://www.example.com, you would use:

sh
Copy code
curl https://www.example.com
To include headers, you might use:

sh
Copy code
curl -H "Accept: application/json" https://www.example.com
To make a POST request with data:

sh
Copy code
curl -X POST -d "name=ferret&color=purple" https://www.example.com
What Happens When You Type google.com in Your Browser (Application Level)
DNS Resolution: The browser queries the DNS to resolve the domain name (google.com) to an IP address.
TCP Connection: The browser establishes a TCP connection to the server at the resolved IP address, usually on port 80 (HTTP) or 443 (HTTPS).
HTTP Request: The browser sends an HTTP GET request to the server for the web page.
Server Processing: The server processes the request and retrieves or generates the requested resource.
HTTP Response: The server sends an HTTP response back to the browser with the status code, headers, and the requested resource (HTML, CSS, JavaScript, etc.).
Rendering: The browser renders the HTML content, fetching additional resources (images, stylesheets, scripts) as needed, and displays the web page to the user.
