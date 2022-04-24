from requests import head
from tabulate import tabulate
import sqlite3
con = sqlite3.connect('user.db')


def InsertData(name,age):
    qry = "insert into user (NAME,AGE) values (?,?);"
    con.execute(qry,(name,age))
    con.commit()
    print("User Details Added")

def UpdateData(id,name,age):
    qry = "update user set NAME=?,AGE=? where ID=?;"
    con.execute(qry,(id,name,age))
    con.commit()
    print("User Details Updated")    

def DeleteData(id):
    qry = "delete from user where ID=?;"
    con.execute(qry,(id))
    con.commit()
    print("User Details Deleted") 

def DisplayData():
    qry = "select ID,NAME,AGE from user;"
    re=con.execute(qry) 
    result= re.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE"]))

def ParticularData(id):
    qry = "select ID,NAME,AGE from user where id=?;"
    de = con.execute(qry,(id))
    res = de.fetchall()
    print(tabulate(res,headers=["ID","NAME","AGE"]))



ch = 0
while ch != 5:
    ch = int(input("\n1.INSERT \n2.UPDATE\n3.DISPLAY\n4.DELETE\n5.PARTICULAR_DATA\n6.EXIT\nYOUR CHOICE:"))
    
    if ch == 1:
        name = input("\nEnter the  NAME  :")
        age = input("\nEnter the Age :")
        InsertData(name,age)

    if ch == 2:
        id = input("\nEnter the ID:")
        name = input("\nEnter the  NAME  :")
        age = input("\nEnter the Age :")
        UpdateData(id,name,age)
   
    if ch == 3:
       DisplayData()

    if ch == 4:
        id = input("\nEnter the ID:")
        DeleteData(id)

    if ch == 5:
        id = input("\nEnter the ID:")
        ParticularData(id)
    
    if ch == 6:
        exit()   
