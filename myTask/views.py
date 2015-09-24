import sqlite3
from myTask import app

@app.route('/') #, methods=['GET'])
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
    print result
    # close the db connection
    conn.close()
    # return data as a string
    return str(result)
    # return 'Hello, Flask!!!'

