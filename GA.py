import random
import itertools
from operator import indexOf
import time

# Permutation Representation
def generate_permutations(nq, size):
    if size <= 0:
        return []

    initial_population = []

    for _ in range(size):
        permutation = list(range(1, nq+1))
        random.shuffle(permutation)
        initial_population.append(permutation)

    return initial_population

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

def cycle_crossover(parent1, parent2):
    n = len(parent1)
    child = [-1] * n
    cycles = [-1] * n

    cycle_num = 1
    index = 0
    for i in range(n):
        index = i
        if cycles[index] == -1: 
            cycles[index] = cycle_num

            while True:
                j = parent2.index(parent1[index])
                cycles[j] = cycle_num
                if i == j:
                    cycle_num += 1
                    break
                index = j

    # create the child
    for i in range(n):
        cycle = cycles[i]
        if cycle % 2 == 1:
            child[i] = parent1[i]
        else:
            child[i] = parent2[i]
    return child

def swap_mutation(x):
    n = len(x)
    idx1, idx2 = random.sample(range(0, n), 2)
    x[idx1], x[idx2] = x[idx2], x[idx1]
    return x

def parent_selection(population):
    tournament = []
    for each in population:
        score = fitness(each)
        tournament.append((each, score))

    tournament.sort(key=lambda x: x[1], reverse=True)   
    # return the best two candidates as parents
    p1, p1_fitness = tournament[0]
    p2, p2_fitness = tournament[1]
    return p1, p2

def genetic_queen(population):
    new_population = []
    L = len(population)
    p_mutation =  1
    
    for i in range(L):
        # select parent
        tournament = random.sample(population, 4)
        parent1, parent2 = parent_selection(tournament)

        # crossover
        child = cycle_crossover(parent1, parent2)
        # mutation
        if random.random() < p_mutation:
            child = swap_mutation(child)
        # evaluate children
        new_population.append(child)

    new_population += population
    # select survivor, pick best L individual
    fitness_scores = [fitness(individual) for individual in new_population]
    sorted_population = [x for _, x in sorted(zip(fitness_scores, new_population), reverse=True)]
    return sorted_population[:L]

# prints given state
def print_state(state):
    print(
        "State = {},  Fitness = {}".format(str(state), fitness(state))
    )

# prints given state board
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
    popSize = 10
    generationSize = 1000
    nq = 8
    maxFitness = (nq * (nq - 1)) / 2  # 8*7/2 = 28

    attacks = 0
    total_time = 0
    hit = 0
    for run in range(runTime):
        start_time = time.time()
        population = generate_permutations(nq, popSize)

        generation = 1
        while (not maxFitness in [fitness(each) for each in population] and generation < generationSize):
            population = genetic_queen(population)
            generation += 1

            fitnessOfstates = [fitness(chrom) for chrom in population]

            beststates = population[
                indexOf(fitnessOfstates, max(fitnessOfstates))
            ]
        end_time = time.time()
        attacks += (maxFitness - fitness(beststates))
        total_time += end_time - start_time
        if maxFitness in fitnessOfstates:
            hit += 1
            print("\nFind optimal solution in Generation {}!".format(generation - 1))

            print_state(beststates)
            #print_board(beststates)

        else:
            print("\nno optimal solution")
            print_state(beststates)
        
    print("\nUsing GA to solve {} queen problem".format(nq))
    print("average attacks = {}/{}, {}".format(attacks, runTime, attacks/runTime))
    print("average running time = {}/{}, {}".format(total_time, runTime, total_time/runTime))
    print("SR = {}/{}, {}".format(hit, runTime, hit/runTime))

