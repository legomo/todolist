import sqlite3
from flask import render_template, request, url_for
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
    return render_template('makeTable.html', rows=result)


@app.route('/new', methods=['GET', 'POST'])
def newTask():
    """
    """
    if request.method == 'POST':
        newTaskName = request.form['task']
        newDescr = request.form['description']
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()

        cursor.execute("INSERT INTO todo (task_name, description, status) VALUES "\
                       "(?,?,?)", (newTaskName, newDescr, 1))

        newID = cursor.lastrowid
        conn.commit()
        cursor.close()

        resp = '<p>The new task was inserted into the database, the ID is: ' \
                '%s</p>' % newID

        return resp
    else:
        return render_template('newTask.html')

