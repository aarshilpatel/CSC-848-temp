#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:42:25 2021

@author: aarshil
"""
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

# Database connection info. Note that this is not a secure connection.
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'aarshilp'
app.config['MYSQL_DATABASE_DB'] = 'sfsu-tutoring-app'
app.config['MYSQL_DATABASE_HOST'] = 'project-1.cxt6ynefb5sw.us-east-2.rds.amazonaws.com'

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

#endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        #book = request.form['book']
        # search by author or book
        cursor.execute("SELECT * from Courses ")
        conn.commit()
        data = cursor.fetchall()
        
    return render_template('search.html', data=data)

@app.route("/")
def main():
    return "Hello world from Flask!"
if __name__ == "__main__":
    app.debug = True
    app.run()
