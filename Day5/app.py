with open('input.txt') as f:
    lines = f.read()


def reduce(units):
    new_units = []
    for i in range(len(units)):
        if len(new_units) > 0 and abs(ord(units[i])-ord(new_units[-1])) == 32:
            new_units.pop()
        else:
            new_units.append(units[i])
    return new_units

# Part 1


reduced = reduce(lines)
print("Part 1:", len(reduced))

# Part 2

min_len = None
for letter in 'abcdefghijklmnopqrstwxyz':

    letter_up = letter.upper()
    units1 = [l for l in lines if l != letter and l != letter_up]

    reduced = reduce(units1)

    if min_len is None or len(reduced) < min_len:
        min_len = len(reduced)

print("Part 2:", min_len)