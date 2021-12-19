from random import randint
from time import time
# if __name__ == '__main__':

#? Input ask
first_multiple_input = input("Rows, columns and tunels: ").rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
k = int(first_multiple_input[2])


#! ---Start--- Board setup
# Legend
print("#: Obstacle")
print("A: Start")
print("M: Mine")
print("%: Exit")
print("W: Free space")

possibilities = ["#", "a", "m", "%"]

# #! TEST ONLY
# board = [
# ['#', '#', '#', '#', '#', '#'],
# ['#', '#', 'a', 'm', '%', '#'],
# ['#', '', (4, 4), '#', '#', '#'],
# ['#', '%', '', '#', '', '#'],
# ['#', '#', '#', '#', (2, 2), '#'],
# ['#', '#', '#', '#', '#', '#']
# ]

#? Board completion
board = []
board.append(["#" for _ in range(m + 2)])

#? Adding rows
for n_itr in range(n):
    row_list = input("Type row: ").rstrip().casefold().split(maxsplit = m)
    row_obstacles = []

    row_obstacles.append("#")
    for space in row_list:
        if space in possibilities:
            row_obstacles.append(space)
        else:
            row_obstacles.append("")

    row_obstacles.append("#")

    board.append(row_obstacles)


board.append(["#" for _ in range(m + 2)])

#? TP setup
for k_itr in range(k):
    second_multiple_input = input("x1, y1, x2, y2: ").rstrip().split()
    i1 = int(second_multiple_input[0])
    j1 = int(second_multiple_input[1])
    i2 = int(second_multiple_input[2])
    j2 = int(second_multiple_input[3])
    board[i1][j1] = (i2, j2)
    board[i2][j2] = (i1, j1)


def printBoard():
    for row in board:
        print("[", end="")
        for index in range(len(row)):
            if index != len(row) - 1:
                print("{:10}".format("\'" + str(row[index]) + "\', "), end="")
            else:
                print("{:10}".format("\'" + str(row[index]) + "\'"), end="")
        print("]")



#! --- Frog setup
start = None
for index in range(len(board)):
    if "a" in board[index]:
        start = (index, board[index].index("a"))
board[start[0]][start[1]] = ""


frog = list(start)

def resetFrog():
    frog[0] = start[0]
    frog[1] = start[1]



#! --- Frog movement

moves_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def moveFrog():
    possible_moves = [[frog[i] + move[i] for i in range(2)] for move in moves_list]
    final_moves = []

    # Remove not available moves
    for move in possible_moves:
        try:
            if board[move[0]][move[1]] == "#":
                continue
            elif move[0] < 0 or move[1] < 0:
                continue
        except:
            continue
        final_moves.append(move)


    if len(final_moves) == 0:
        return "blocked"

    choose_move = randint(0, len(final_moves) - 1)

    for i in range(2):
        frog[i] = final_moves[choose_move][i]

    return "free"




#! --- Frog in exit or mine

def checkFrog():
    place_check = board[frog[0]][frog[1]]
    if place_check == "m":
        return "mine"
    elif place_check == "%":
        return "exit"
    elif type(place_check) == tuple:
        return "tp"

# x: possible moves to complete the laberinth
def resultOfPath(x: int):
    resetFrog()
    for _ in range(x):
        situation = moveFrog()
        if situation == "blocked":
            return False

        check = checkFrog()
        if check == "mine":
            return False

        elif check == "exit":
            return True

        elif check == "tp":
            place = board[frog[0]][frog[1]]
            for i in range(2):
                frog[i] = place[i]

    return None



#! --- Code
t_plays = 10
plays = []

print("Please wait while we process the answer ...")
for _ in range(t_plays):
    plays.append(resultOfPath(100))


# print(plays)
printBoard()

exited = plays.count(True)
#escape_prob = exited / (t_plays - plays.count(None))
if(t_plays - plays.count(None) != 0):
    escape_prob = exited / (t_plays - plays.count(None))
else:
    escape_prob = 0

print("Probability that the frog escapes: {:10}".format(escape_prob))

#! Multiprocessing module para meter más repeticiones