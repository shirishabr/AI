import heapq

# Get Initial and Goal states from user
print("Enter Initial State (9 numbers, use 0 for blank space):")
INITIAL_STATE = tuple(map(int, input().split()))

print("Enter Goal State (9 numbers, use 0 for blank space):")
GOAL_STATE = tuple(map(int, input().split()))

class Node:
    def __init__(self, board, g=0, h=0, parent=None):
        self.board = board
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f


# Heuristic 1: Misplaced Tiles
def misplaced_tiles(board, goal):
    count = 0
    for i in range(len(board)):
        if board[i] != 0 and board[i] != goal[i]:
            count += 1
    return count


# Heuristic 2: Manhattan Distance
def manhattan_distance(board, goal):
    distance = 0
    for i in range(len(board)):
        val = board[i]
        if val != 0:
            target_idx = goal.index(val)
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(target_idx, 3)
            distance += abs(r1-r2) + abs(c1-c2)
    return distance


def get_successors(node, goal, heuristic_fn):
    successors = []
    blank_idx = node.board.index(0)
    r, c = divmod(blank_idx, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_blank_idx = nr * 3 + nc
            new_board = list(node.board)

            new_board[blank_idx], new_board[new_blank_idx] = (
                new_board[new_blank_idx], new_board[blank_idx]
            )

            new_board_tuple = tuple(new_board)
            h = heuristic_fn(new_board_tuple, goal)

            successors.append(
                Node(new_board_tuple, node.g + 1, h, node)
            )

    return successors


def a_star_search(initial_state, goal_state, heuristic_fn):
    open_list = []
    closed_set = set()

    initial_h = heuristic_fn(initial_state, goal_state)
    root = Node(initial_state, 0, initial_h)

    heapq.heappush(open_list, root)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.board in closed_set:
            continue

        closed_set.add(current_node.board)

        if current_node.board == goal_state:
            path = []
            curr = current_node

            while curr:
                path.append(curr)
                curr = curr.parent

            return path[::-1]

        for neighbor in get_successors(
            current_node, goal_state, heuristic_fn
        ):
            if neighbor.board not in closed_set:
                heapq.heappush(open_list, neighbor)

    return None


def print_board(board):
    for i in range(0, 9, 3):
        row = [str(x) if x != 0 else ' ' for x in board[i:i+3]]
        print(" | ".join(row))


def print_solution_path(path):
    if path is None:
        print("No solution found!")
        return

    for step, node in enumerate(path):
        print(f"Step {step} (g={node.g}, h={node.h}, f={node.f}):")
        print_board(node.board)
        print("-" * 15)


# Validate input
if (len(INITIAL_STATE) != 9 or len(GOAL_STATE) != 9
        or set(INITIAL_STATE) != set(range(9))
        or set(GOAL_STATE) != set(range(9))):
    print("Invalid input! Enter numbers 0 to 8 exactly once.")
else:

    # Case 1: Misplaced Tiles
    print("\n=== CASE 1: Misplaced Tiles Heuristic ===")
    path_case1 = a_star_search(
        INITIAL_STATE, GOAL_STATE, misplaced_tiles
    )
    print_solution_path(path_case1)

    # Case 2: Manhattan Distance
    print("\n=== CASE 2: Manhattan Distance Heuristic ===")
    path_case2 = a_star_search(
        INITIAL_STATE, GOAL_STATE, manhattan_distance
    )
    print_solution_path(path_case2)
