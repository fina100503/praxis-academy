from flask import Flask
from flask import render_template
from flask import request
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="*finaalia1053")
    
    curs = conn.cursor()    
    if request.method == "POST":
        nama = request.form["nama"]
        detail = request.form["detail"]
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)   # untuk mengeksekusi query
        conn.commit()

    print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    # data = ["apel", "anggur", "amer"] ==> dummy (data percobaan) bisa dimatikan fungsinya
    return render_template("/homse.html", context=data)

@app.route("/detail/<buah_id>")
def detail(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="*finaalia1053")
    
    curs = conn.cursor()
    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    print(data)
    return""

if __name__ == "__main__":
    app.run()

        # print(request.method)
        # print(20*"=")
        # print(request.form)
        # print(request.form["nama"])
        # print(request.form["detail"])
        # print(20*"=")