#!/usr/bin/env python3
# TODO: I think that only one board can win per turn, which is causing boards to fill up too quickly

import copy
from pprint import pprint
from sys import argv

filename = argv[1]

boards = []
board_states = {}
game_numbers = []
already_won = []
winning_states = {}


def parse_game(game_input):
    current_board = []
    for line in game_input:
        # we need to get the winning numbers
        if len(game_numbers) == 0:
            for num in line.split(','):
                game_numbers.append(int(num.strip()))

        # we've parsed the winning numbers time to parse the boards
        else:
            # we've found the beginning of a board
            if len(line) <= 2:
                # put the current board into the game boards if it has numbers
                if len(current_board) > 0:
                    board_states[len(boards)] = empty_state_board()
                    boards.append(current_board)

                # reset the current board
                current_board = []
            else:
                current_board.append([int(n.strip())
                                     for n in line.split(' ') if len(n) > 0])

    # pickup the last board in the list
    board_states[len(boards)] = empty_state_board()
    boards.append(current_board)


def is_game_finished():
    print("len boards", len(boards))
    print("len already won", len(already_won))
    for state in board_states:
        verticals = [[], [], [], [], []]
        # check horizontals
        for row in board_states[state]:
            if all(n == 1 for n in row) and state not in already_won:
                already_won.append(state)
                return (True, state)
            v_index = 0
            for n in row:
                verticals[v_index].append(n)
                v_index += 1

        # check verticals
        for col in verticals:
            if all(n == 1 for n in col) and state not in already_won:
                already_won.append(state)
                return (True, state)
    return (False, None)


def mark_number_on_board(target_num, board_index, board):
    row_index = 0
    for row in board:
        if target_num in row:
            board_states[board_index][row_index][row.index(target_num)] = 1
        row_index += 1


def run_turn():
    if len(game_numbers) > 0:
        target_num = game_numbers.pop(0)
        print(f"Running turn: {target_num}")

        board_index = 0
        for board in boards:
            mark_number_on_board(target_num, board_index, board)
            board_index += 1
    return target_num


def sum_uncalled_numbers(state_index, state_copy=None):
    tboard = boards[state_index]
    tstate = board_states[state_index]
    tsum = 0

    if state_copy:
        tstate = state_copy

    for y in range(0, 5):
        for x in range(0, 5):
            if tstate[x][y] == 0:
                tsum += tboard[x][y]

    return tsum


def empty_state_board():
    return [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def run_game(part1=True):
    last_winning_board = None
    last_winning_state = None
    last_winning_num = None

    while len(game_numbers) > 0:
        print(game_numbers)
        target_num = run_turn()
        check_finish = is_game_finished()

        if part1:
            if check_finish[0]:
                print("WE'VE WON")
                print("part1: ", target_num *
                      sum_uncalled_numbers(check_finish[1]))
                break
        else:
            if check_finish[0]:
                print("A BOARD WON", check_finish[1])
                pprint(boards[check_finish[1]])
                pprint(board_states[check_finish[1]])
                print(already_won)
                last_winning_num = target_num
                last_winning_state = copy.deepcopy(
                    board_states[check_finish[1]])
                last_winning_board = check_finish[1]

    if not part1:
        print(last_winning_num)
        pprint(last_winning_state)
        print("part2: ", last_winning_num *
              sum_uncalled_numbers(last_winning_board, state_copy=last_winning_state))


if __name__ == "__main__":
    with open(filename) as input_file:
        parse_game(input_file.readlines())
        run_game(part1=False)
