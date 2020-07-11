# Prompt user for text

text = input("Text: ")

# Initialization
letters = 0
words = 1
sentences = 0
length = len(text)

# Iterating over text
for i in range(length):
    p = text[i]
    # For Letters
    if p.isalpha():
        letters += 1
    else:
        # For words
        if (p == ' '):
            words += 1
        # For Sentences
        elif (p == '.' or p == '?' or p == '!'):
            sentences += 1

# Average letters per 100 words
L = ((letters / words) * 100)
# Average sentences per 100 words
S = ((sentences / words) * 100)
# Formulae for calculating readability
index = round((0.0588 * L) - (0.296 * S) - 15.8)

if (index < 1):
    print("Before Grade 1")
elif (1 <= index and index < 16):
    print("Grade {}".format(index))
else:
    print("Grade 16+")

