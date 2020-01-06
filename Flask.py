#pip install flask
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/') #returns hello world
def index():
    return 'hello world'

@app.route('/hello/<name>') #returns the name variable in the URL
def helloname(name):
    return 'Hello %s' % name

@app.route('/user/<name>') #if the name passed is admin or guest redirect to a different page
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

@app.route('/admin') #Used by @app.route('/user/<name>')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest') #Used by @app.route('/user/<name>')
def hello_guest():
    return 'Hello Guest'

#Run the app
if __name__ == "__main__":
    app.run()

#Run with Python (scriptname.py) from console CMD/PowerShell