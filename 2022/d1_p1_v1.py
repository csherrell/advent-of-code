with open("d1-p1-input.txt") as file:
    df = file.readlines()
max = -1
calories = 0
for line in df:
    line = line.strip()
    if line:
        calories += int(line)
    else:
        if calories > max:
            max = calories
        calories = 0
print(f"Max: { max }")
