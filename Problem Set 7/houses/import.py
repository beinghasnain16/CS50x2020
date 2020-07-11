# DONE
from sys import argv, exit
from cs50 import SQL
import csv

# Command line argument
if len(argv) != 2:
    print("Usage:/ python import.py characters.csv")
    exit(1)

# parsing
file = argv[1]
# connecting to database
db = SQL("sqlite:///students.db")

# reading csv file
data = []
with open(file, 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        data.append(r)
    data.pop(0)

# iterating for query
for student in data:
    name = student[0].split()
    query = "INSERT INTO students (first, middle, last, house, birth) VALUES("
    if len(name) == 1:
        query += f"'{name[0]}', NULL, NULL, "
    elif len(name) == 2:
        query += f"'{name[0]}', NULL, '{name[1]}', "
    else:
        query += f"'{name[0]}', '{name[1]}', '{name[2]}', "
    query += f"'{student[1]}', {student[2]});"
    db.execute(query)
