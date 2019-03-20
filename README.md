# CGI-Python
## This repo contains the programs written in Python.
### CGI The Common Gateway Interface (CGI) is a standard for writing programs that can interact through a 
Web server with a client running a Web browser.
1. CGI is the standard for programs to interface with HTTP servers.
2. CGI programming is written dynamically generating webpages that respond to user input or 
webpages that interact with software on the server.

To install apache on your system refer the following link:
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04-quickstart

#### To run cgi program follow the steps below:

CGIHTTPRequestHandler can be enabled in the command line by passing the --cgi option:
python3 -m http.server --bind localhost --cgi 8000

Put your script into "cgi_directories":
This defaults to ['/cgi-bin', '/htbin'] and describes directories to treat as containing CGI scripts.

Open in the browser:
$ python -mwebbrowser http://localhost:8000/cgi-bin/(The name of your file)


