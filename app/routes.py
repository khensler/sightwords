from flask import current_app as app
from flask import render_template, redirect, flash, request
import random
import sqlite3
import os

dbpath = os.environ.get('DB_PATH')
if dbpath is None:
    dbpath = "words.db"

@app.route('/')
@app.route('/index')
def index():
     return render_template('words.html',word='Welcome')

@app.route('/word')
def word():
     conn = sqlite3.connect(dbpath)
     c = conn.cursor()
     c.execute("select word from words where correct <= incorrect order by incorrect ASC limit 5")
     rows = c.fetchall()
     words = []
     for row in rows:
          words.append(row[0])
     c.execute("select word from words where correct >= incorrect order by correct ASC limit 5")
     rows = c.fetchall()
     words = []
     for row in rows:
          words.append(row[0])
          print(row[0])
     return random.choice(words)

@app.route("/report/<word>/<report_val>")
def report(word, report_val):
     conn = sqlite3.connect(dbpath)
     c = conn.cursor()
     c.execute('''select correct, incorrect from words where word = ?''', [word])
     row = c.fetchone()
     correct = row[0]
     incorrect = row[1]
     if report_val == "0":
          incorrect = incorrect +1
     if report_val == "1":
          correct = correct +1
     c.execute("update words set correct = ? , incorrect = ? where word = ?",(correct, incorrect, word))
     conn.commit()
     return "ok"

@app.route("/word/incorrect")
def get_incorrect_words():
     conn = sqlite3.connect('words.db')
     c = conn.cursor()
     c.execute("select word from words correct order by correct ASC limit 10")
     rows = c.fetchall()
     words = []
     for row in rows:
          words.append(row[0])
     return random.choice(words)

@app.route("/results")
def get_results():
     conn = sqlite3.connect('words.db')
     c = conn.cursor()
     c.execute("select word, correct, incorrect from words order by correct DESC")
     rows = c.fetchall()
     words = []
     for row in rows:
          if row[2]>0 and row[1] > 0:
               word_dict = {
                    'word' : row[0],
                    'correct' : row[1],
                    'incorrect' : row[2],
                    'percentage' : round(100*(row[1]/(row[1]+row[2])),0)
               }
          else:
               word_dict = {
                    'word' : row[0],
                    'correct' : row[1],
                    'incorrect' : row[2],
                    'percentage' : '0'
               }
          print(word_dict)
          words.append(word_dict.copy())
     return render_template("results.html", words=words)
