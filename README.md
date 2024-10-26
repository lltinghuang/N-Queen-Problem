# N-Queen-Problem
solve with Iterative Deepening Search (IDS),  Hill Climbing (HC), and Genetic Algorithm (GA)

## Experiment 
### n = 8
|            | IDS     | HC      | GA      |
|------------|---------|---------|---------|
| Average attacks      | 0       | 0.466   | 0       |
| Average running time | 0.114004 | 0.000553 | 0.008054 |
| Success rate (SR)    | x       | 0.533   | 1.0     |

### n = 50
|                        | IDS | HC       | GA       |
|------------------------|-----|----------|----------|
| Average attacks        | x   | 0.566    | 0        |
| Average running time   | x   | 3.171316 | 5.551241 |
| Success rate (SR)      | x   | 0.5      | 1.0      |

## Implementation
### IDS
- Implements iterative deepening search (IDS) by repeatedly calling DLS with increasing depth limits.
- **DLS**
  - Initial state: empty board
  - Action: put a queen on the board
  - Goal: there are n queens on the board, and they don’t attack each other
  - **Idea**:  
    Initialize a list of length n with each position set to -1, indicating that the position is empty. The list `state[i]` is used to record the row where the queen in column i is placed.  
    Starting with an empty chessboard (root), at each depth, only one queen is placed, ensuring that each column has only one queen. When searching for successors, it tests whether placing a queen at a particular position would result in an attack, ensuring that placing a queen in that position is "legal".  
    When queens have been placed in all columns (each position is legal without mutual attacks), and the sum of the values recorded in the state list is \(0 + 1 + 2 + \dots + n\), our goal is reached. Thus, we return the state as the optimal solution.

### HC
- **State representation**: permutation
- **Initial state**: generates an initial random permutation of numbers from 1 to n
- **Neighbor state**: swapping the position of two queens in the current state
- **Evaluate function**: calculates the fitness of a given state by counting the number of diagonal collisions between queens. The maximum fitness is \(n \times (n - 1) / 2\), representing the number of non-attacking pairs of queens.
- **Idea**: iteratively explores neighboring states and moves to the neighbor with the highest fitness if it has a higher fitness than the current state. The process stops when no better neighbors are found.
- **Run time**: 30, as required.

### GA
- **Parameters**:
  - runtime = 30
  - population size = 10
  - generation = 1000
  - representation = permutation
  - selection = tournament
  - crossover = cycle crossover with rate 1
  - mutation = swap mutation with rate 1
  - survivor = Fitness-Based Selection

- **Fitness function**:  
  Evaluates the fitness of a given state (permutation) by counting the number of diagonal collisions between queens.

- **Idea**:  
  The GA is implemented based on the method and parameters mentioned in the paper. Permutations are used to represent the positions of queens on the chessboard, and ten random permutations are generated as the initial population.  
  In each generation, four individuals are randomly selected as a subset, from which the top two individuals with the best fitness scores are chosen as parents. These parents undergo cycle crossover and swap mutation to generate offspring. The fitness of both parents and offspring is compared, and the top ten individuals are selected to proceed to the next generation. This process is repeated for 1000 generations.

- **Experiments and parameters**:  
  These parameters are effective for both 8-queen and 50-queen problems, so no changes were made in the experiments.
