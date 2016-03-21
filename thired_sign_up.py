# Import modules for CGI handling 
import cgi
import cgitb
from Sql_Module import student as a

#print("Content-Type: text/plain\n\n")
cgitb.enable()

# Create instance of FieldStorage 
form = cgi.FieldStorage()

#path = "C:\Python27\thired.html"

#print path
First_name = form.getvalue('First_name')
Last_name  = form.getvalue('Last_name')
User_name = form.getvalue('User_name')
Password = form.getvalue('Password')
Address  = form.getvalue('Address')
Phone  = form.getvalue('Phone')
Email = form.getvalue('Email')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "Hello!! Welcome To Our world."
print "</head>"
print "<h3>Hello %s, %s</h3>" % (First_name,Last_name)

s().insert(First_name,Last_name,User_name,Password,Address,Phone,Email)
