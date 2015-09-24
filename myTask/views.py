import sqlite3
from flask import render_template
from myTask import app

@app.route('/')
@app.route('/tasks', methods=['GET'])
def getTasks():
    """
    """
    # open db
    conn = sqlite3.connect(app.config['DATABASE'])
    # Get the cursor
    cursor = conn.cursor()
    # SQL query to fetch the data
    cursor.execute("select * from todo;")
    # Fetch the data
    result = cursor.fetchall()
    # close the db connection
    conn.close()
    # return data as a string
    return str(result)

@app.route('/temp', methods=['GET'])
def getTemplate():
    """
    """
    # open db
    conn = sqlite3.connect(app.config['DATABASE'])
    # Get the cursor
    cursor = conn.cursor()
    # SQL query to fetch the data
    cursor.execute("select * from todo;")
    # Fetch the data
    result = cursor.fetchall()
    # close the db connection
    conn.close()
    # return data as a string
    return render_template('test.html', rows=result)

