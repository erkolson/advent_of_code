#!/usr/bin/env python3

game_boards = "game-boards.txt"
game_input = "91,17,64,45,8,13,47,19,52,68,63,76,82,44,28,56,37,2,78,48,32,58,72,53,9,85,77,89,36,22,49,86,51,99,6,92,80,87,7,25,31,66,84,4,98,67,46,61,59,79,0,3,38,27,23,95,20,35,14,30,26,33,42,93,12,57,11,54,50,75,90,41,88,96,40,81,24,94,18,39,70,34,21,55,5,29,71,83,1,60,74,69,10,62,43,73,97,65,15,16"

def parse_boards(input):
    boards = []
    with open(input) as fd:
        board_string = ""
        for line in fd:
            if line == "\n":
                boards.append(GameBoard(board_string))
                board_string = ""
                continue
            # print(f"line={line}")
            board_string += line
    return boards

class GameBoard:
    values = [[]]
    scores = [[]]
    size   = 0
    won    = False

    def __init__(self, board_string, size=5):
        self.size = size
        self.values = [[ 0 for i in range(size)] for j in range(size)]
        self.scores = [[ 0 for i in range(size)] for j in range(size)]

        board_list = board_string.split()
        for i in range(0,size):
            for j in range(0,size):
                self.values[i][j] = int(board_list[i*size + j])

    def __str__(self):
        return f"board={self.values}\nscore={self.scores}"

    def are_ya_winning_son(self):
        # rows
        streaks = [row for row in self.scores]
        # columns
        streaks.extend([[row[j] for row in self.scores] for j in range(0,self.size)])
        # diagonals
        streaks.append([self.scores[i][i] for i in range(0,self.size)])
        streaks.append([self.scores[self.size - 1 -i][i] for i in range(self.size-1,-1,-1)])

        # print(f"streaks={streaks}")

        for row in streaks:
            if row.count(1) == 5:
                # print("winner winner chicken dinner")
                self.won = True
                return self.won
        return None

    # tally them scores
    def score(self, val):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.values[i][j] == val:
                    self.scores[i][j] = 1
                    # https://www.youtube.com/watch?v=aPEqasj1uMI
                    break

    def unmarked_sum(self):
        sum = 0
        for i in range(0,self.size):
            for j in range(0,self.size):
                if self.scores[i][j] == 0:
                    sum += self.values[i][j]
        return sum

boards = parse_boards(game_boards)

for num in game_input.split(','):
    print(f"input={num}")
    for board in boards:
        if not board.won:
            board.score(int(num))
            # print(board)
            game_won = board.are_ya_winning_son()
            if game_won:
                print(f"winning board = {board}")
                print(f"num={int(num)}, sum={board.unmarked_sum()}")
                score = int(num) * board.unmarked_sum()
                print(f"score={score}")
