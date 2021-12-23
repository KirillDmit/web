from flask import Flask, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)


@app.route("/")
def cv_index():
    cvs = get_cv()
    res = ""
    for i, cv in enumerate(cvs):
        res += f"<h1>{i + 1})</h1>"
        res += f"<p>Желаемая зарплата: {cv['salary']}.</p>"
        res += f"<p>Образование: {cv['educationType']}.</p>"

    return res


@app.route("/dashboard")
def dashboard():
    return render_template('d1.html')


@app.route("/dashboard")
def dashboard():
    return render_template('d2.html',
                           cvs=get_cv(),
                           )


def dict_factory(cursor, row):
    # обертка для преобразования
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_cv():
    con = sqlite3.connect('works.sqlite')
    con.row_factory = dict_factory
    res = list(con.execute('select * from works limit 3'))
    con.close()
    return res


app.run()
