try:
    import psycopg2
    conn = psycopg2.connect(host="localhost",
        database="contoh",
        user="postgres",
        password="*finaalia1053")



    curs = conn.cursor()

    nama = "angga"
    umur = 22
    query = f"insert into santri(nama, umur) values('{nama}', {umur})"

    curs.execute(query)
    conn.commit()
    print("data masuk")
except Exception as e:
    print(e)
