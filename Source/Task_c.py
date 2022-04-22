SIZE = 8

def createRowCNF():
    row = []

    # create CNF clauses for rows
    for i in range(SIZE):

        # CNF for the current row; ie: 1 v 2 v 3 v 4 v 5 v 6 v 7 v 8
        row.append([(i * SIZE + j + 1) for j in range(SIZE)])

        # CNF for each pair of the row; ie: -1 ^ -2, -1 ^ -3
        for x in range(SIZE - 1):
            for y in range(x + 1, SIZE):
                temp1 = i * SIZE + x + 1
                temp2 = i * SIZE + y + 1
                row.append([-temp1, -temp2])
    return row

def createColumnCNF():
    col = []

    # create CNF clauses for columns
    for i in range(SIZE):
        # CNF for the current column; ie: 1 v 9 v 17 v 25 v 33 v 41 v 49 v 57
        col.append([(j * SIZE + i + 1) for j in range(SIZE)])

        # CNF for each pair of the column; ie: -1 ^ -9, -1 ^ -17
        for x in range(SIZE - 1):
            for y in range(x + 1, SIZE):
                temp1 = x * SIZE + i + 1
                temp2 = y * SIZE + i + 1
                col.append([-temp1, -temp2])
    
    return col

def createDiagonalCNF():
    diag = []
    # create CNF clauses for 2 diagonals
    # primary diagonal: y = x - m
    # secondary diagonal: y = -x + m + 7
    temp = SIZE - 2     # temp = 6

    # from -6 to 0 (7 primary diagonal and 7 secondary diagonal)
    for m in range(-temp, 1):    
        for i in range(SIZE - abs(m) - 1):
            for j in range(i + 1, SIZE - abs(m)):
                # CNF for each pair of primary diagonal
                x1 = i
                x2 = j
                y1 = x1 - m
                y2 = x2 - m
                diag.append([ -(x1 * SIZE + y1 + 1), -(x2 * SIZE + y2 + 1) ])

                # CNF for each pair of secondary diagonal
                y1 = -(x1 - m - (SIZE - 1))
                y2 = -(x2 - m - (SIZE - 1))
                diag.append([ -(x1 * SIZE + y1 + 1), -(x2 * SIZE + y2 + 1) ])
                

    # from 1 to 6 (6 primary diagonal and 6 secondary diagonal)
    for m in range(1, temp + 1):   
        for i in range(m, SIZE - 1):
            for j in range(i + 1, SIZE):
                # CNF for each pair of primary diagonal
                x1 = i
                x2 = j
                y1 = x1 - m
                y2 = x2 - m
                diag.append([ -(x1 * SIZE + y1 + 1), -(x2 * SIZE + y2 + 1) ])

                # CNF for each pair of secondary diagonal
                y1 = -(x1 - m - (SIZE - 1))
                y2 = -(x2 - m - (SIZE - 1))
                diag.append([ -(x1 * SIZE + y1 + 1), -(x2 * SIZE + y2 + 1) ])
    return diag

def Level1():
    col = createColumnCNF()
    f = open("Level1_CNF.txt", "w")

    # write row CNF
    for item in col:
        for subitem in item:
            f.write(str(subitem))

            if subitem != item[-1]:
                f.write("v")
        f.write("\n")


    f.close()

def Level2():
    row = createRowCNF()
    col = createColumnCNF()
    diag = createDiagonalCNF()
    f = open("Level2_CNF.txt", "w")

    # write row CNF
    for item in row:
        for subitem in item:
            f.write(str(subitem))

            if subitem != item[-1]:
                f.write("v")
        f.write("\n")

    # write column CNF
    for item in col:
        for subitem in item:
            f.write(str(subitem))

            if subitem != item[-1]:
                f.write("v")
        f.write("\n")

    # write diagonals CNF
    for item in diag:
        for subitem in item:
            f.write(str(subitem))

            if subitem != item[-1]:
                f.write("v")
        f.write("\n")
    f.close()


def main():
    Level1()
    Level2()
    
if __name__ == "__main__":
    main()
    print('Level1_CNF.txt and Level2_CNF.txt files have been created!')
    input()