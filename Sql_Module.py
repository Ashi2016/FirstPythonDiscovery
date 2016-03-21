import MySQLdb,cgi,cgitb
connection = MySQLdb.connect("127.0.0.1","root","tiger","python2")

cursor = connection.cursor()
class student:
   def __init__(self):
      pass
   def delete(self,Email):
      self.Email = Email  
      cursor.execute("""delete from people where First_name = %s;"""(self.Email))
      connection.commit()
      connection.close()
   def insert(self,First_name, Last_name, User_name, Password, Address, Phone, Email):
      self.First_name = First_name
      self.Last_name = Last_name
      self.User_name = User_name
      self.Password = Password
      self.Address = Address
      self.Phone = Phone
      self.Email = Email
      cursor.execute("""insert into people values (%s,%s,%s,%s,%s,%s,%s)""",(self.First_name,self.Last_name,self.User_name,self.password,self.Address,self.Phone,self.Email))
      connection.commit()
      connection.close()
   def select(self):
      count=0
      cursor.execute("select * from people;")
      for row in cursor:
         print row
         count=count+1
           #print count
      connection.close()
          
   def update(self,First_name, Last_name, User_name, Password, Address, Phone, Email):
      self.First_name = First_name
      self.Last_name = Last_name
      self.User_name = User_name
      self.Password = Password
      self.Address = Address
      self.Phone = Phone
      self.Email = Email
      cursor.execute("""update people set name=%s where id=%s%s%s%s%s%s%s""",(self.First_name,self.Last_name,self.User_name,self.password,self.Address,self.Phone,self.Email))
      connection.commit()
      connection.close()
         
if __name__ == "__main__":
    print "pakku"

s = student
