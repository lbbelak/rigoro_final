from csv import reader


def isbn_format(number) -> bool:
    total = 0
    weight = 10
    for digit in number:
        if digit == 'X':
            total += 10 * weight
        else:
            total += int(digit) * weight
        weight += -1
    if total % 11 == 0:
        return True
    return False


FILE_NAME = "tNmieVFn.csv"                  # Pri cislovani nevalidnich
rows = []                                   # radku v testech, je chyba
with open(FILE_NAME, 'r') as csv_file:      # Error! 3 column(s) on line 185!
    all_objects = reader(csv_file)          # se nachazi na radku 184!
    row_index = 0
    for row in all_objects:
        fields = str(row).split(';')
        fields[0] = fields[0][2:]
        fields[-1] = fields[-1][:-1]
        rows.append(row)
        if len(fields) != 4:
            print("Error! " + str(len(fields)) +
                  " column(s) on line " + str(row_index) + "!")
        elif not fields[0].strip():
            print("Missing title on line: " + str(row_index))
        elif not fields[1].strip():
            print("Missing author on line: " + str(row_index))
        elif not fields[2].strip():
            print("Missing ISBN on line: " + str(row_index))
        elif len(fields[2]) != 10:
            print("Invalid ISBN on line: " + str(row_index))
        elif not isbn_format(fields[2]):
            print("Invalid ISBN on line: " + str(row_index))
        elif not fields[3].strip():
            print("Missing price on line: " + str(row_index))
        elif "â‚¬" not in fields[3] and "KÄŤ" not in fields[3]:
            print("Invalid price on line: " + str(row_index))
        elif "," not in fields[3] and "." not in fields[3]:
            print("Invalid price on line: " + str(row_index))
        row_index += 1
