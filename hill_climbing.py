def count_attacking_pairs(state):
    """Calculates the cost function: number of pairs of queens attacking each other."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Same row conflict
            if state[i] == state[j]:
                conflicts += 1
            # Diagonal conflict
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def print_board(state):
    """Displays 4x4 chessboard layout for state array."""
    n = len(state)
    for r in range(n):
        row_str = "|"
        for c in range(n):
            if state[c] == r:
                row_str += " Q |"
            else:
                row_str += "   |"
        print(row_str)

def hill_climbing_4queens(initial_state):
    current = list(initial_state)
    current_cost = count_attacking_pairs(current)
    step = 0
   
    print("=== INITIAL STATE ===")
    print(f"State: {current}")
    print(f"Cost (Attacking Pairs): {current_cost}")
    print_board(current)
    print("-" * 35)

    while True:
        step += 1
        n = len(current)
        best_neighbor = None
        best_cost = float('inf')
        best_swap = None

        print(f"\nStep {step}: Evaluating Neighbors (by swapping pairs)...")

        # Systematically generate neighbors using queen position swaps
        # Evaluated in lexicographical order (x0,x1), (x0,x2), (x0,x3), (x1,x2), etc.
        for i in range(n):
            for j in range(i + 1, n):
                neighbor = list(current)
                # Swap row positions of queen i and queen j
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                cost = count_attacking_pairs(neighbor)
               
                print(f"Swap (x{i}, x{j}) -> State: {neighbor}, Cost: {cost}")

                # Tie-breaking rule: strict '<' maintains the smallest index pair
                if cost < best_cost:
                    best_cost = cost
                    best_neighbor = neighbor
                    best_swap = (i, j)

        print(f"\n--> Best Neighbor selected: Swap {best_swap} -> State: {best_neighbor} with Cost = {best_cost}")

        # If best neighbor does not strictly improve the cost, algorithm terminates (local minimum/goal)
        if best_cost >= current_cost:
            print("\nAlgorithm Terminated: No better neighbor found (Local Minimum or Goal reached).")
            break

        current = best_neighbor
        current_cost = best_cost

        print(f"Updated Current State: {current} (Cost: {current_cost})")
        print_board(current)
        print("-" * 35)

    print("\n=== FINAL RESULT ===")
    print(f"Final State: {current}")
    print(f"Final Cost: {current_cost}")
    if current_cost == 0:
        print("Status: Goal Configuration Reached Successfully!")
    else:
        print("Status: Terminated at Local Minimum.")

# Execute with the exact initial state from the PDF
initial_state = [3, 1, 2, 0]
hill_climbing_4queens(initial_state)