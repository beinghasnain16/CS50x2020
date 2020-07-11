# DONE
from sys import argv, exit
from cs50 import SQL

# command line argument
if len(argv) != 2:
    print("Usage:/ python roster.py HouseName")
    exit(1)

house = argv[1]

# connecting to database
db = SQL("sqlite:///students.db")

for student in db.execute('SELECT first,middle,last,birth FROM students WHERE house=? ORDER BY last, first', house):
    if student['middle'] != None:
        print("{} {} {}, born {}".format(student['first'], student['middle'], student['last'], student['birth']))
    else:
        print("{} {}, born {}".format(student['first'], student['last'], student['birth']))