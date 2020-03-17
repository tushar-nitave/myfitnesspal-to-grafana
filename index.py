import os
from flask import Flask, request, render_template, url_for, redirect
import pandas as pd
import sqlalchemy as db
import pymysql
import myfitnesspal
import datetime
from calendar import monthrange
import flask

pymysql.install_as_MySQLdb()

app = Flask(__name__)


@app.route("/")
def fileFrontPage():
    return render_template('index.html', status="N/A", file="N/A")


@app.route('/getdata', methods = ['POST'])
def getdata():

    username = request.form['text']

    client = myfitnesspal.Client(username)

    with open("nurition_data.csv", "w") as file:
        file.write("Date\tCals\tCarbs\tFat\tProtein\tSodium\tSugar\t")
        file.write("\n")
        for month in range(1, 4):
            print("Current Month: {}".format(month))
            for day in range(1, monthrange(2020, month)[1]):
                macros = client.get_date(2020,month,day)
                if len(macros.totals) != 0:
                    macros = macros.totals
                    date = "2020/"+str(month)+"/"+str(day)
                    file.write(date)
                    file.write("\t")
                    print(date)
                    for i, j in macros.items():
                        file.write(str(j))
                        file.write("\t")
                    file.write("\n")
                    date = ""
    file.close()
    return render_template('index.html', status="success", file="nutrition_data.csv")
   

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'file' in request.files:
        data = request.files['file']
        if data.filename != '':  
            data = pd.read_csv(data.filename, sep="\t")
            engine = db.create_engine("mysql://myfitnesspal:root@localhost:3306/data")

            data.to_sql(name="macros", con=engine, if_exists='replace')

    return redirect(url_for("grafana"))


@app.route("/grafana")
def grafana():
    return render_template("/grafana.html")


if __name__ == '__main__':
    app.run(debug=True)

    
    
    
    