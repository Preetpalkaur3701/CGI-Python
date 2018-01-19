#!/usr/bin/python
import cgi, cgitb 
import math

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
l = int(form.getvalue('length'))
b = int(form.getvalue('breath'))
h = int(form.getvalue('height'))
r = int(form.getvalue('radius'))
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Table</title>"
print "</head>"
print "<body>"
print "<h2>area of rectangle " + "</h2>"
print "<p> %s X %s  = %s</p>" % (l, b,  l * b)
print "<h2>volume of cuboid " + "</h2>"
print "<p> %s X %s  x %s = %s</p>" % (l, b ,h ,  l * b * h)
print "<h2>perimeter of rectangle " + "</h2>"
print "<p> %s X %s X %s = %s<  /p>" % (l, b, 2 ,2 * l * b)
print "<h2>area of circle" + "</h2>"
print "<p> %s X %s X %s = %s</p>" % (math.pi , r ,r, math.pi * r *r)
print "<h2>area of triangle" + "</h2>"
print "<p> %s X %s X %s = %s</p>" % (l, b, 0.5, l * b * 0.5)
print "<h2>area of square " + "</h2>"
print "<p> %s X %s = %s</p>" % (l,l, l * l)
print "</body>"
print "</html>" 