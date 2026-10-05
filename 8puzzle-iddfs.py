def moves(state):
    result = []

    p = state.index(0)

    # Move UP
    if p >= 3:
        s = state[:]
        s[p], s[p-3] = s[p-3], s[p]
        result.append(s)

    # Move DOWN
    if p < 6:
        s = state[:]
        s[p], s[p+3] = s[p+3], s[p]
        result.append(s)

    # Move LEFT
    if p % 3 != 0:
        s = state[:]
        s[p], s[p-1] = s[p-1], s[p]
        result.append(s)

    # Move RIGHT
    if p % 3 != 2:
        s = state[:]
        s[p], s[p+1] = s[p+1], s[p]
        result.append(s)

    return result


def dfs(state, goal, depth, visited):

    if state == goal:
        return True

    if depth == 0:
        return False

    visited.add(tuple(state))

    for next_state in moves(state):

        if tuple(next_state) not in visited:
            if dfs(next_state, goal, depth - 1, visited):
                return True

    return False


def iddfs(start, goal):

    depth = 0

    while True:

        visited = set()

        print("Depth:", depth)

        if dfs(start, goal, depth, visited):
            print("Goal Found!")
            break

        depth += 1


# Input
print("Enter initial state:")
start = list(map(int, input().split()))

print("Enter goal state:")
goal = list(map(int, input().split()))

iddfs(start, goal)







