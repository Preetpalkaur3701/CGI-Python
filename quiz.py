#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
score = 0
# Get data from fields
q1 = str(form.getvalue('q1'))
if (q1 == "a"):
    score += 1
q2 = str(form.getvalue('q2'))
if (q2 == "b"):
    score += 1
q3 = str(form.getvalue('q3'))
if (q3 == "a"):
    score += 1
q4 = str(form.getvalue('q4'))
if (q4 == "b"):
    score += 1
q5 = str(form.getvalue('q5'))
if (q5 == "a"):
    score += 1
q6 = str(form.getvalue('q6'))
if (q6 == "a"):
    score += 1
q7 = str(form.getvalue('q7'))
if (q7 == "b"):
    score += 1 
q8 = str(form.getvalue('q8'))
if (q8 == "b"):
    score += 1
q9 = str(form.getvalue('q9'))
if (q9 == "c"):
    score += 1
q10 = str(form.getvalue('q10'))
if (q10 == "b"):
    score += 1

print "Content-type:text/html\r\n\r\n"

print "<html>"
print "<head>"
print "<title>What Preetpal likes the most?</title>"
print "</head>"
print "<body>"
print "<p>Total score = %s</p>" % (score)
print "</body>"
print "</html>"
