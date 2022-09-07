from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="jurnal_umum",
        user="postgres",
        password="*finaalia1053")
    
    curs = conn.cursor()    
    if request.method == "POST":
        tanggal = request.form.get("tanggal")
        keterangan = request.form.get("keterangan")
        debit = request.form.get("debit")
        kredit = request.form.get("kredit")
        query = f"insert into koperasi(tanggal, keterangan, debit, kredit) values('{tanggal}', '{keterangan}', '{debit}', '{kredit}')"
        curs.execute(query)   # untuk mengeksekusi query
        conn.commit()

    print(request.method)
    query = f"select * from koperasi"
    curs.execute(query)
    data = curs.fetchall()
    curs.close()
    conn.close()
    # data = ["apel", "anggur", "amer"] ==> dummy (data percobaan) bisa dimatikan fungsinya
    return render_template("index.html", context=data)

if __name__ == "__main__":
    app.run()

        # print(request.method)
        # print(20*"=")
        # print(request.form)
        # print(request.form["nama"])
        # print(request.form["detail"])
        # print(20*"=")