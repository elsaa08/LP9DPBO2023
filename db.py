import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="lp9"
)

dbcursor = mydb.cursor()

sql = "INSERT INTO test (nama, adress) VALUES (%s, %s)"
val = ("Elsa", "jl Cilimus")
dbcursor.execute(sql, val)

mydb.commit()
print(dbcursor.rowcount, "record inserted.")

dbcursor = mydb.cursor()

dbcursor.execute("SELECT * FROM test")
myresult=dbcursor.fetchall()
for x in myresult:
    print(x)

sql = "DELETE FROM test WHERE nama = 'Elsa'"
#sql= ("VolKnoo")
dbcursor.execute(sql)
mydb.commit()
print(dbcursor.rowcount, "records deleted.")


dbcursor.execute("SELECT * FROM test")
myresult=dbcursor.fetchall()
for x in myresult:
    print(x)