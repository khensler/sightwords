from flask import current_app as app
from flask import render_template, redirect, flash, request
import random
import sqlite3

words = ["a",
"an",
"and",
"as",
"is",
"look",
"can",
"me",
"to",
"come",
"day",
"down",
"go",
"for",
"I",
"am",
"see",
"no",
"had",
"her",
"he",
"the",
"in",
"his",
"it",
"if",
"like",
"him",
"into",
"made",
"about",
"my",
"good",
"not",
"on",
"run",
"big",
"up",
"two",
"at",
"all",
"are",
"be",
"but",
"by",
"call",
"yes",
"one",
"play",
"could",
"did",
"do",
"said",
"each",
"find",
"first",
"may",
"more",
"get",
"has",
"two",
"up",
"we",
"been",
"you",
"have",
"from",
"how",
"long",
"make",
"number",
"now",
"say",
"she",
"so",
"some",
"that",
"there",
"how",
"with",
"way",
"over",
"than",
"time",
"who",
"write",
"part",
"out",
"these",
"water",
"then",
"their",
"use",
"away",
"blue",
"black",
"funny",
"here",
"little",
"new",
"of",
"please",
"red",
"saw",
"too",
"under",
"want",
"white",
"yellow",
"they",
"this",
"oil",
"other",
"people",
"was",
"your",
"were",
"what",
"would",
"which",
"when",
"word",
"them",
"are",
"brown",
"came",
"green",
"jump",
"must",
"out",
"pretty",
"ride",
"ran",
"soon",
"three",
"well",
"went",
"where",
"help",
"four"
]



@app.route('/')
@app.route('/index')
def index():
     return render_template('words.html',word='Welcome')

@app.route('/word')
def word():
     conn = sqlite3.connect('words.db')
     c = conn.cursor()
     c.execute("select word from words where correct <= incorrect limit 5")
     rows = c.fetchall()
     words = []
     for row in rows:
          words.append(row[0])
     c.execute("select word from words where correct >= incorrect limit 5")
     rows = c.fetchall()
     words = []
     for row in rows:
          words.append(row[0])
     return random.choice(words)

@app.route("/report/<word>/<report_val>")
def report(word, report_val):
     conn = sqlite3.connect('words.db')
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