
import random
import math

# Count conflicts
def conflicts(board):
    count = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                count += 1

    return count


# Simulated Annealing
def simulated_annealing():

    n = int(input("Enter number of queens: "))
    board = list(map(int, input("Enter initial positions: ").split()))

    if n < 4 or len(board) != n or any(x < 0 or x >= n for x in board):
        print("Invalid input!")
        return

    T = 100
    alpha = 0.99
    cost = conflicts(board)

    print("Initial Board:", board)
    print("Initial Conflicts:", cost)

    best = board.copy()
    best_cost = cost

    for _ in range(100000):

        if best_cost == 0:
            break

        new = board.copy()
        col = random.randint(0, n - 1)
        new[col] = random.randint(0, n - 1)

        new_cost = conflicts(new)
        delta = new_cost - cost

        if delta <= 0 or random.random() < math.exp(-delta / T):
            board = new
            cost = new_cost

        if cost < best_cost:
            best = board.copy()
            best_cost = cost

        T *= alpha

        if T < 0.01:
            board = best.copy()
            cost = best_cost
            T = 100

    print("\nFinal Board:", best)
    print("Final Conflicts:", best_cost)

    if best_cost == 0:
        print("Solution Found!")
        for i in range(n):
            for j in range(n):
                print("Q" if best[j] == i else "-", end=" ")
            print()
    else:
        print("Solution not found!")


simulated_annealing()
