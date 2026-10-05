def moves(state):
    result = []

    p = state.index(0)

    # UP
    if p >= 3:
        s = state[:]
        s[p], s[p-3] = s[p-3], s[p]
        result.append(s)

    # DOWN
    if p < 6:
        s = state[:]
        s[p], s[p+3] = s[p+3], s[p]
        result.append(s)

    # LEFT
    if p % 3 != 0:
        s = state[:]
        s[p], s[p-1] = s[p-1], s[p]
        result.append(s)

    # RIGHT
    if p % 3 != 2:
        s = state[:]
        s[p], s[p+1] = s[p+1], s[p]
        result.append(s)

    return result


def dfs(start, goal):

    stack = [start]
    visited = set()

    while stack:

        state = stack.pop()

        if state == goal:
            print("Goal Found!")
            return

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        print(state)

        for next_state in moves(state):
            if tuple(next_state) not in visited:
                stack.append(next_state)

    print("Goal Not Found")


# Input
print("Enter initial state:")
start = list(map(int, input().split()))

print("Enter goal state:")
goal = list(map(int, input().split()))

dfs(start, goal)