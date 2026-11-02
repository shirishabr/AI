
def count_attacking_pairs(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def print_board(state):
    n = len(state)

    for r in range(n):
        row = ""
        for c in range(n):
            if state[c] == r:
                row += " Q "
            else:
                row += " . "
        print(row)


def hill_climbing(initial_state, goal_state):
    current = list(initial_state)
    current_cost = count_attacking_pairs(current)
    step = 0

    print("\nINITIAL STATE")
    print("State:", current)
    print("Cost:", current_cost)
    print_board(current)

    if current == goal_state:
        print("\nGoal Reached!")
        return

    visited = {tuple(current)}

    while True:
        n = len(current)
        best_neighbor = None
        best_cost = float('inf')

        # Generate neighbors by swapping queen positions
        for i in range(n):
            for j in range(i + 1, n):
                neighbor = current.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

                if tuple(neighbor) in visited:
                    continue

                cost = count_attacking_pairs(neighbor)

                if cost < best_cost:
                    best_cost = cost
                    best_neighbor = neighbor

        # Check whether goal is reached
        if best_neighbor == goal_state:
            current = best_neighbor
            current_cost = best_cost
            step += 1

            print(f"\nSTEP {step}")
            print("State:", current)
            print("Cost:", current_cost)
            print_board(current)
            print("\nGOAL STATE REACHED!")
            return

        # Stop if no better neighbor exists
        if best_neighbor is None or best_cost >= current_cost:
            print("\nGoal not reached!")
            print("Hill Climbing stopped at Local Minimum.")
            break

        current = best_neighbor
        current_cost = best_cost
        visited.add(tuple(current))
        step += 1

        print(f"\nSTEP {step}")
        print("State:", current)
        print("Cost:", current_cost)
        print_board(current)

        if current == goal_state:
            print("\nGOAL STATE REACHED!")
            return

    print("\nFINAL STATE:", current)
    print("FINAL COST:", current_cost)


# User Input
n = int(input("Enter number of Queens (N): "))

print("Enter Initial State:")
initial_state = list(map(int, input().split()))

print("Enter Goal State:")
goal_state = list(map(int, input().split()))

# Validation
if (n < 1 or len(initial_state) != n or len(goal_state) != n
        or sorted(initial_state) != list(range(n))
        or sorted(goal_state) != list(range(n))):
    print("Invalid Input! Enter numbers from 0 to N-1 exactly once.")

else:
    hill_climbing(initial_state, goal_state)
