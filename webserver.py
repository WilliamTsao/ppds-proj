#!/usr/bin/python3

from flask import Flask, render_template, request
from datetime import datetime
import urllib
app = Flask(__name__)

import MySQLdb as mdb

con = mdb.connect(host = 'localhost', 
                  user = 'root',
                  database = 'citibike2',
                  passwd = 'dwdstudent2015', 
                  charset='utf8', use_unicode=True);




@app.route('/')
def home():
    return('hi')


@app.route('/<station_id>')
def station(station_id):
    cur=con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Docks_Status WHERE station_id="+station_id+" ORDER BY last_communication_time DESC")
    status = cur.fetchall()
    cur.close()
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT station_name FROM Docks WHERE station_id = "+station_id)
    name = cur.fetchall()
    cur.close()
    return render_template('station_status.html', status= status, name = name[0]['station_name'])


app.run(host='0.0.0.0', port=8000, debug=True)

