from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config.from_pyfile('config.local.py', silent=True)

import myTask.views 

