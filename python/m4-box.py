width = int(input("How wide is your box?\n"))
height = int(input("How high is you box?\n"))

out_row = " * " * width
mid_width = width -2
mid_rows = "*" + ' ' * mid_width + "*"

print(out_row + '\n' + (mid_rows + '\n') * height + out_row)