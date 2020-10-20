message = "lbh zhfg hayrnea jung lbh unir yrnearq"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

symbol = message
for key in range(len(LETTERS)):
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        num = num - key
        if num <0:
            num = num + len(LETTERS)
        symbol = symbol + LETTERS[num]
    else:
        symbol = symbol + LETTERS[num]


print(symbol)