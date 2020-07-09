matrix = [
    [ 7 , " ",  3 ],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["i", "r", "!"]
]

text = ""
invalid_letter_count = 0

def is_valid(letter):
    return type(letter) is str and letter.isalnum()

for col in range(3):
    for row in matrix:
        letter = row[col]

        if is_valid(letter):
            if invalid_letter_count > 1:
                invalid_letter_count = 0
                text += " "
            text += letter
        else:
            invalid_letter_count += 1

print(text)    