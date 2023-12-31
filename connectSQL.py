import pyodbc
from Scrapper import scrap1
cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" 
                      "Server=DESKTOP-PG6D1VU\\SQLEXPRESS;" 
                      "Database=WebScrapper;" 
                      "Trusted_Connection=yes;"

                      )

# Create a cursor
cursor = cnxn.cursor()
#Call function scap1 in Scrapper.py
my_data = scrap1()

#Convert the list of dictionaries into list of tuples
myList = []
for i in range(len(my_data)):
    myList1 = []
    for value in (my_data[i].values()):
     myList1.append(value)
    myList1 = tuple(myList1)
    myList.append(myList1)
#l = len(my_data)
#print(l)
# Prepare and execute the SQL INSERT statement
#for i in range(l):
#    sql_insert = f"INSERT INTO Scrap1 (title, excerpt, pub_date) VALUES ('{my_data['title'][i]}', '{my_data['excerpt'][i]}', '{my_data['pub_date'][i]}')"
#    cursor.execute(sql_insert)

#insert_query = "INSERT INTO Scrap(title,excerpt,pub_date) VALUES ( %(title)s, %(excerpt)s, %(pub_date)s);"
#cursor.executemany(insert_query, my_data)

#mySqlStr = f'INSERT INTO Scrapped(title, excerpt, pub_date) VALUES(?,?,?)'

#Create Table and Insert Table
cursor.execute("CREATE TABLE Scrapped1(title VARCHAR(255), excerpt VARCHAR(MAX), pub_date VARCHAR(255))")
mySqlStr = f'INSERT INTO Scrapped1(title, excerpt, pub_date) VALUES(?,?,?)'
cursor.executemany(mySqlStr, myList)


# Commit the changes and close the connection
cnxn.commit()
cnxn.close()