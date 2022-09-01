try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="*finaalia1053")



    curs = conn.cursor()

    namaLama = "anggang"

    query = f"delete for santri where nama='{nama}'"
    curs.execute(query)
    conn.commit()
    print("data berhasil dihapus")
except Exception as e:
    print(e)
