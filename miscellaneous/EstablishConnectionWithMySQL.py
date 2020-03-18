import mysql.connector

mysql_db = mysql.connector.connect(host = "localhost", user = "root", passwd = "root", database = "mfdb")
if mysql_db != None:
    print("Connection is Established")
    print(mysql_db)
## END

mysql_cursor = mysql_db.cursor()
if mysql_cursor != None:
    print("Cursor is available")
    print(mysql_cursor)
## END

mysql_cursor.execute('SELECT "ABCD"')

# mysql_cursor.execute("SELECT * FROM COFFEES")
# result = mysql_cursor.fetchall()

# for record in result:
#     print(record)
## END

# jarhead
# saving private ryan
# 

mysql_cursor.close()
mysql_db.close()
