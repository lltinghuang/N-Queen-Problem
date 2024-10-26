import random
from itertools import combinations
import time

def initialize(nq):
    permutation = list(range(1, nq+1))
    random.shuffle(permutation)

    return permutation

def fitness(state):
    diagonal_collisions = 0
    n = len(state)
    maxFitness = n * (n-1) // 2
    # Check diagonal collisions in both directions
    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == abs(i - j):
                diagonal_collisions += 1
    return maxFitness - diagonal_collisions

def find_neighbors(state):
    neighbors = []

    for i, j in combinations(range(len(state)), 2):
        neighbor = state.copy()  
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i] 
        neighbors.append(neighbor)
    return neighbors

def hill_climbing(nq):
    current = initialize(nq)
    while True:
        neighbors = find_neighbors(current)
        if not neighbors:
            break
        # shuffle(neighbours)
        fitness_scores = [fitness(each) for each in neighbors]
        sorted_neighbors = [x for _, x in sorted(zip(fitness_scores, neighbors), reverse=True)]
        best_neighbor = sorted_neighbors[0]
        if fitness(best_neighbor) > fitness(current):
            current = best_neighbor
        else:
            break

    return current

def print_state(chrom):
    print("state = {},  Fitness = {}".format(str(chrom), fitness(chrom)))

def print_board(chrom):
    board = []

    for x in range(nq):
        board.append(["x"] * nq)

    for i in range(nq):
        board[chrom[i]-1][i-1] = "Q"

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print()
    print_board(board)

if __name__ == "__main__":
    runTime = 30
    nq = 8
    maxFitness = (nq * (nq - 1)) / 2  # 8*7/2 = 28

    attacks = 0
    total_time = 0
    hit = 0
    for run in range(runTime):
        start_time = time.time()
        local_opt = hill_climbing(nq)
        end_time = time.time()
        total_time += end_time - start_time
        local_score = fitness(local_opt)
        attacks += (maxFitness - local_score)
        if local_score == maxFitness:
            hit += 1
            print("\nFind optimal solution!")
            print_state(local_opt)
            # print_board(local_opt)

        else:
            print("\nno optimal solution")
            print_state(local_opt)
    print("\nUsing HC to solve {} queen problem".format(nq))
    print("average attacks = {}/{}, {}".format(attacks, runTime, attacks/runTime))
    print("average running time = {}/{}, {}".format(total_time, runTime, total_time/runTime))
    print("SR = {}/{}, {}".format(hit, runTime, hit/runTime))

