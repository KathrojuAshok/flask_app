from flask import Flask, render_template

import pandas as pd
import os
import numpy as np

os.chdir("D:\\flask\\eff_flask")

from graph import build_graph

students=pd.read_excel("students.xlsx")

students.columns

students.columns[0:5]

students=students[students.columns[0:5]]

total_students=students['Student Name'].value_counts().sum()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html',ts=total_students)

@app.route('/subjects')
def subjects():
    return render_template("subjects.html",subjects=students.columns[1:5])

@app.route('/<subject>')
def graphs(subject):
    #These coordinates could be stored in DB
    x=students['Student Name']
    y1=students[subject]


    graph1_url = build_graph(x,y1);
   

    return render_template('template.html',name1=subject,graph1=graph1_url)


if __name__ == '__main__':

    app.run(debug=True,use_reloader=False)