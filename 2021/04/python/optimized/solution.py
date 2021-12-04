#!/usr/bin/env python3

import copy
from pprint import pprint
from sys import argv

filename = argv[1]


def parse_input_file(input_file):
    win_num = []
    boards = []
    current_board = []

    for line in input_file:
        # we haven't read the first line of winning numbers
        if len(win_num) == 0:
            win_num = [int(n) for n in line.strip().split(',')]

        else:
            # a new line means we've found a new board
            if len(line) <= 2 and len(current_board) > 0:
                boards.append(current_board)
                current_board = []
            elif len(line) > 2:
                current_board.append([int(n) for n in line.strip().split()])

    # grab the last board
    if len(current_board) > 0:
        boards.append(current_board)

    return win_num, boards


def check_if_winner(all_boards, part2=False):
    winning_boards = []

    b_index = 0
    for board in all_boards:
        board_won = False
        v_list = [[], [], [], [], []]
        # check horizontal
        for row in board:
            if all(n == 0 for n in row) and not board_won:
                winning_boards.append(board)
                del(all_boards[b_index])
                board_won = True
            for n in row:
                v_list[row.index(n)].append(n)

        # check veritical
        for row in v_list:
            if all(n == 0 for n in row) and not board_won:
                winning_boards.append(board)
                del(all_boards[b_index])
        b_index += 1

    return winning_boards


def run_turn(target_num, all_boards):
    for board in all_boards:
        for y in range(0, 5):
            for x in range(0, 5):
                if board[x][y] == target_num:
                    board[x][y] = 0


if __name__ == "__main__":
    part2 = True

    with open(filename) as input_file:
        win_num, boards = parse_input_file(input_file)

        last_winning_num = None
        last_winning_board = None

        for num in win_num:
            run_turn(num, boards)
            winning_boards = check_if_winner(boards)

            if len(winning_boards) > 0:
                if not part2:
                    board_sum = sum(sum(winning_boards[0], []))
                    print(f"win num: {num}")
                    print(f"board sum: {board_sum}")
                    print(f"part1: {board_sum * num}")
                    break
                else:
                    last_winning_num = num
                    last_winning_board = copy.deepcopy(winning_boards[-1])

        if part2:
            board_sum = sum(sum(last_winning_board, []))
            print(f"win num: {last_winning_num}")
            print(f"board sum: {board_sum}")
            print(f"part2: {board_sum * last_winning_num}")
