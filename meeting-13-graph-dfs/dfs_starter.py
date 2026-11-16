
def dfs(maze, start, goal):
    """Return (path, visited, max_frontier); path is None if unreachable.
    visited: set of expanded positions. Path includes start and goal.
    """
    frontier = [start]
    visited = set()
    parents = {start: None}
    max_frontier = 1

    while frontier:
        current = frontier.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            path = reconstruct_path(parents, start, goal)
            return (path, visited, max_frontier)

        for neighbor in neighbors(maze, current):
            if neighbor not in visited and neighbor not in parents:
                parents[neighbor] = current
                frontier.append(neighbor)

        max_frontier = max(max_frontier, len(frontier))

    return (None, visited, max_frontier)
