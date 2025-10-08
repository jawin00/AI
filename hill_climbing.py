import random

def fitness(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def hill_climbing(n):
    board = random.sample(range(n), n)
    while True:
        current_fitness = fitness(board)
        neighbors = []
        for i in range(n):
            for j in range(n):
                if j != board[i]:
                    new_board = board[:]
                    new_board[i] = j
                    neighbors.append(new_board)
        neighbors.sort(key=lambda x: fitness(x))
        best_neighbor = neighbors[0]
        if fitness(best_neighbor) < current_fitness:
            board = best_neighbor
        else:
            break
    return board

n = 8
solution = hill_climbing(n)
print(solution)
