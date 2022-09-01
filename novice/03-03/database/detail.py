# try:
import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="contoh",
        password="*finaalia1053")

# except Exception as e:
    # print(e)

curs = conn.cursor()
query = f"select *from santri where nama='angga'"
curs.execute(query)
data = curs.fetchone()
if not data:
    print("gak ada")
else:
    print("nama:", [0], "umur:", [1])

