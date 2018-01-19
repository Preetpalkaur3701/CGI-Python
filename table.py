#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
table_no = int(form.getvalue('no'))
range_from = int(form.getvalue('rf'))
range_to = int(form.getvalue('rt'))

print "Content-type:text/html\r\n\r\n"


print "<html>"
print "<head>"
print "<title>Table</title>"
print "</head>"
print "<body>"
print "<h2>Table of " + str(table_no) + "</h2>"
for i in range(range_from , range_to + 1):
    print "<p> %s X %s = %s</p>" % (table_no, i, (table_no) * i)
print "</body>"
print "</html>"
