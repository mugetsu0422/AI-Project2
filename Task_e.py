
# from operator import truediv
# import queue
# import math
# import re


SIZE = 8

#Read from file and take 2 number at the same time for the index of our n-first queen(s)
def read_coordinate(file_name):
    result = []
    f = open(file_name, 'r')
    n = int(f.readline())
    line = f.readline()
    tempQ = []

    for item1 in line.split(')'):
        for item2 in item1.split(','):
            tempQ.append(item2.strip('() '))

    for i in range(n):
        x = int(tempQ.pop(0))
        y = int(tempQ.pop(0))
        result.append([x, y])

    return result

def initial_state(board, queens):
    if len(queens) > 0:
        for item in queens:
            x = item[0]
            y = item[1]
            board[x][y] = True

    return board

def initial_state_2(queens):
    board = [[ False for i in range(SIZE) ] for j in range(SIZE)]

    if len(queens) > 0:
        for item in queens:
            x = item[0]
            y = item[1]
            board[x][y] = True

    return board


def print_state(board):
    str = ''

    for i in range(SIZE):
        temp = ''

        for j in range(SIZE):
            if board[i][j]:
                temp += 'Q '

            else:
                temp += '. '

        temp += '\n'
        str += temp

    print(str)

def is_possible(row, col, board):
    # Check in the same row and colunm
    for item in range(SIZE):
        if board[item][col]  and item != row :
            return False

        if board[row][item]  and item != col :
            return False

    # Check 2 diagonals
    for item in range(-SIZE, SIZE + 1):
        if item == 0:
            continue

        x = row + item
        y = col + item

        if x >= 0 and x < SIZE and y >=0 and y < SIZE:
            if board[x][y] :
                return False

        x = row - item
        y = col + item

        if x >= 0 and x < SIZE and y >= 0 and y < SIZE:
            if board[x][y] :
                return False

    return True

# Check if the queens have attack each orthers or not
def is_valid(board):
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] and not is_possible(i,j,board):
                return False
    return True

# Heruistic
def heuristic_value(queens):
    h = 0
    board = [[ False for i in range(SIZE) ] for j in range(SIZE)]
    initial_state(board,queens)

    for i in range(SIZE):
        for j in range(SIZE):
            if is_possible(i,j,board) and not board[i][j] :
                h += 1
    return h
    
# Find the suitable cell(s) left
def get_suitable_cell(board):
    cells = []

    for i in range(SIZE):
        if sum(board[i]) == 0:
            for j in range(SIZE):
                if is_possible(i,j,board):
                    cells.append((i,j))

            return cells

    return cells

def is_goal(board, queens):
    return len(queens) == SIZE and is_valid(board)

def sort_queue(queue):
    for i in range(len(queue)):
        min_ind = i

        for j in range(len(queue)):
            if heuristic_value(queue[min_ind]) < heuristic_value(queue[j]):
                min_ind = j

            queue[i], queue[min_ind] = queue[min_ind], queue[i]

    return queue
        
# A* algorithm function
def A_star(board, queens):
    queue = []
    visited = []

    for item in queens:
        visited.append(item)
    
    queue.append(queens)
    current = []

    while len(queue) > 0 :

        current = queue.pop(0)
        board = initial_state_2(current)

        if is_goal(board, current):
            return current
        
        successors = get_suitable_cell(board)

        for item in successors:
            if item not in visited:
                temp = []
                visited.append(item)
                current.append(item)

                for item in current:
                    temp.append(item)

                queue.append(temp)
                current.pop()
        queue = sort_queue(queue)

    return None


def main():
    file_name = input("Enter file name: ")

    board = [[ False for i in range(SIZE) ] for j in range(SIZE)]
    queens = read_coordinate(file_name)

    board = initial_state(board, queens)
    print("Initial State: ")
    print_state(board)

    queens = A_star(board, queens)

    if queens is None:
        print("No solution")

    else:
        print("Final State")
        board = initial_state(board,queens)
        print_state(board)


if __name__ == "__main__":
    main()
    input()