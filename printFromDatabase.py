import sqlite3

key = "python"

conn = sqlite3.connect('results.db')
cursor = conn.cursor()
cursor.execute("SELECT id, text FROM res WHERE key='"+key+"'")

nr = 0
while True:
    row = cursor.fetchone()
    if row == None:
        break
    print(100*"=")
    print("nr=", nr, "-> id = ", row[0])
    print(row[1])
    print(100*"=")
    nr += 1