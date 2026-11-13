import mysql.connector

print("started")

try:
    conn = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="Kapil@123",
        database="batch19"
    )

    if conn.is_connected():
        print("CONNECTED DB SUCCESSFULLY")

        cursor = conn.cursor()

        query = "insert into dbemployee2(id,name,salary) values(%s,%s,%s)"

        data = [
            (102, 'rashmika', 90000),
            (103, 'katappa', 7770),
            (104, 'raju', 765545)
        ]

        cursor.executemany(query, data)

        # single record insert
        cursor.execute("insert into dbemployee2 values(105,'deepika',90000)")

        conn.commit()

        print("inserted successfully")

        cursor.close()
        conn.close()

except Exception as e:
    print("connection issue:", e)

print("done with code")