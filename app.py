from flask import Flask, render_template, request, session, redirect
import sqlite3
import time

app = Flask(__name__)
app.secret_key = b'sgwt26t1uqan82'

@app.route('/')
def index():
      return render_template('homepage.html')
      
@app.route('/sign-up', methods = ['POST'])
def signUp():
   username = request.form.get('username')
   password = request.form.get('password')

   conn = sqlite3.connect("database.sqlite")
   c = conn.cursor()
   c.execute('select * from user where userName = ?;', (username,))
   existing = c.fetchone()

   if existing:
    conn.close()
    return render_template('homepage.html', error = 'This username is taken. Try another one', trigger_signUpOverlay=True)
   else:
     c.execute('insert into user(userName, passwordHash, points) values(?, ?, ?)',
                 (username, password, 0,))
     conn.commit()
     c.execute('select userID from user where userName = ?;', (username,))
     user = c.fetchone()
     session['userID'] = user[0]
     conn.close()
   return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
   username = request.form.get('username')
   password = request.form.get('password')

   conn = sqlite3.connect("database.sqlite")
   c = conn.cursor()
   c.execute('select * from user where userName = ? and passwordHash = ?;', (username, password,))
   account = c.fetchone()
   conn.close()

   if account:
    session['userID'] = account[0]
    return redirect('/')
   else:
      return render_template('homepage.html', error = 'Invalid username or password. Please try again', trigger_overlay=True)

@app.route('/logout')
def logout():
   session.clear()
   return redirect('/')

@app.route('/lessons')
def lessonPage():
      return render_template('lessons.html')

@app.route('/stories')
def stories():
      return render_template('stories.html')

@app.route('/about')
def about():
      return render_template('about.html')
          
