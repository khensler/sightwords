import sqlite3

conn = sqlite3.connect('words.db')
c = conn.cursor()
#c.execute('''DROP TABLE tiles''')
c.execute('''CREATE TABLE if not exists tiles (id integer PRIMARY KEY AUTOINCREMENT, tile_name text NOT NULL);''')
#conn.commit
#w_val="numbers"
#c.execute('''INSERT INTO tiles(tile_name) VALUES(?)''',(w_val,))
#conn.commit
c.execute('''CREATE TABLE if not exists words (word text, correct real, incorrect real, tile_id integer)''')
#c.execute('''ALTER TABLE words ADD COLUMN tile_id''')
conn.commit

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

numbers = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "70",
    "71",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "96",
    "97",
    "98",
    "99",
    "100"
]

#for num in numbers:
#    c.execute("INSERT INTO words VALUES(?,?,?,?)",(num,0,0,"2"))

print("tiles:")
c.execute("select * from tiles")
rows = c.fetchall()
for row in rows:
    print(row)
print("words:")
c.execute("select * from words")
rows = c.fetchall()
for row in rows:
    print(row)

conn.commit()