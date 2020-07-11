# Importing external libraries
from sys import argv, exit
import csv

# Command line arguments
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

# Function for counting maximum SRTs


def max_count(sequence, STR):
    max_count = 0
    l = len(STR)
    i = sequence.find(STR)
    for i in range(len(sequence)):
        count = 0
        if sequence[i:i+l] == STR:
            count += 1
            while sequence[i:i + l] == sequence[i + l:i + 2 * l]:
                count += 1
                i += l

        if count > max_count:
            max_count = count

    return str(max_count)


# Filenames from cmd arguments
csvFile = argv[1]
textFile = argv[2]

# Reading files
# Arranging data in dictionary data structure
temp = []
with open(csvFile) as csvfile:
    reader = csv.DictReader(csvfile)
    for dct in map(dict, reader):
        temp.append(dct)
dicts = {}
for f in temp:
    dicts[f['name']] = f
    del dicts[f['name']]['name']

with open(csvFile) as f:
    strs = f.readline().strip().split(',')
    strs.pop(0)

with open(textFile, 'r') as f:
    sequence = f.read()
occurences = {}

for i in strs:
    occurences[i] = max_count(sequence, i)

maxCount = max(occurences, key=occurences.get)

# Comparing sequences with data from database
for d in dicts:
    for str, count in dicts[d].items():
        if (str, count) == (maxCount, occurences[maxCount]):
            if dicts[d] == occurences:
                print(d)
                exit(0)
print("No match")
exit(0)

