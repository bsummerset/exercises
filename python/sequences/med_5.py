text = "WHEN PROGRAMMING SLEEP IS OVERRATED"
replacements = [('A','4'), ('E', '3'), ('G' ,'6'), ('I', "1"), ('O', '0'), ('S', '5'), ('T', '7')]
new_string = text

for letter, number in replacements:
    new_string = new_string.replace(letter,number)

print(new_string)