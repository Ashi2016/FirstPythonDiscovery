import MySQLdb,cgi,cgitb

cgitb.enable()
print "Content-type: text/html"

form = cgi.FieldStorage()

User_name = form.getvalue('User_name')
Password = form.getvalue('Password')
First_name = form.getvalue('First_name')
Last_name  = form.getvalue('Last_name')
print User_name,Password

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "Hello!! Welcome To Our world."
print "</head>"
print "</html>"
#print "<h3>Hello %s, %s</h3>" % (First_name,Last_name)

database = MySQLdb.connect('127.0.0.1','root','tiger','python2') 

cursor = database.cursor()

#print "<h3>Hello %s, %s</h3>" % (First_name,Last_name)

cursor.execute("select User_name,Password from people")

data = list(cursor.fetchall())
count = 0
while (data == User_name or Password):
    print "Successful."
    count = count + 1
else:
    print "access denied."
