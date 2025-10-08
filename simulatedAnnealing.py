import random
import math

def fitness(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def simulated_annealing(n):
    board = random.sample(range(n), n)
    current_temp = n
    min_temp = 0.1
    cooling_rate = 0.99
    while current_temp > min_temp:
        current_fitness = fitness(board)
        new_board = board[:]
        i, j = random.sample(range(n), 2)
        new_board[i], new_board[j] = new_board[j], new_board[i]
        new_fitness = fitness(new_board)
        if new_fitness < current_fitness or random.random() < math.exp((current_fitness - new_fitness) / current_temp):
            board = new_board
        current_temp *= cooling_rate
    return board

n = 8
solution = simulated_annealing(n)
print(solution)
