import time
def is_valid_move(state, row, col):
    if row in state:
        return False

    # Check for conflicts in the diagonals
    for i in range(col):
        if state[i] == row or abs(state[i] - row) == abs(i - col):
            return False

    return True

def find_successors(state, col):
    n = len(state)
    next_states = []
    for row in range(n):
        if is_valid_move(state, row, col):
            new_state = state.copy()
            new_state[col] = row
            next_states.append(new_state)
    return next_states


def DLS(state, depth):
    states = []
    n = len(state)
    stateNode = (state, 0)
    states.append(stateNode)
    visited = []

    while states:
        curState, curDepth = states.pop()
        if curDepth > depth:
            continue # pass this state
        if sum(curState) == (n * (n - 1)) // 2:
            return curState
        if curState not in visited:
            visited.append(curState)
            successors = find_successors(curState, curDepth)
            for child in successors:
                newNode = (child, curDepth+1)
                states.append(newNode)
    return None

def IDS(nq):
    root = [-1] * nq #permutation representation [0, 7]
    for depth in range(nq+1):
        print("start running depth:", depth)
        found = DLS(root, depth)
        if found:
            return found
        else:
            print("no solution in depth:", depth)

# prints given state board
def print_board(chrom):
    board = []

    for x in range(nq):
        board.append(["x"] * nq)

    for i in range(nq):
        board[chrom[i]][i] = "Q"

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print()
    print_board(board)


if __name__ == "__main__":
    nq = 8

    total_time = 0
    start_time = time.time()
    solution = IDS(nq) 
    end_time = time.time()  
    total_time = end_time - start_time    
    if solution:
        print("Find the solution: ", solution)
    print("\nUsing IDS to solve {} queen problem".format(nq))
    if solution: 
        print("average attacks = {}".format(0))
    print("average running time = {}".format(total_time))
        

