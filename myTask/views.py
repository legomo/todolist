import sqlite3
from flask import render_template, request, url_for
from myTask import app

@app.route('/temp', methods=['GET'])
def getTemplate():
    """
    This view function gets task data from the database and uses a template to
    render the data formatted into a table for better prsentation.
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


@app.route('/edit/<int:idNo>', methods=['GET', 'POST'])
def updateTask(idNo):
    """
    """
    if request.method == 'POST':
        taskEdit = request.form['task']
        descriptionEdit = request.form['description']
        statusEdit = request.form['status']

        if statusEdit == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute("UPDATE todo SET task_name = ?, description = ?, "\
                       "status = ? WHERE id LIKE ?", (taskEdit, descriptionEdit,
                                                      status, idNo))
        conn.commit()

        resp = '<p>The item number %s was successfully updated</p>' % idNo

        return resp
    else:
        conn = sqlite3.connect(app.config['DATABASE'])
        cursor = conn.cursor()
        cursor.execute("SELECT task_name FROM todo WHERE id LIKE ?",
                       (str(idNo)))
        curData = cursor.fetchone()

        return render_template('editTask.html', old=curData, idNo=idNo) 


@app.route('/')
@app.route('/temp', methods=['GET'])
def getTasks():
    """
    This page handler / view function gets tasks data form the database and
    returns a list of tuples to the requestor.
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

