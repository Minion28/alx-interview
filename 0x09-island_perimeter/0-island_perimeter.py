#!/usr/bin/python3
"""
island_perimeter
"""


def island_perimeter(grid):
    """
    Determine perimeter of an island
    """
    visit = set()

    if not grid:
        return 0

    def dfs(x, y):
        """
        depth first search
        """
        if (x, y) in visit:
            return 0
        if x >= len(grid) or\
                y >= len(grid[0]) or\
                x < 0 or y < 0 or\
                grid[x][y] == 0:
            return 1
        visit.add((x, y))
        result = dfs(x, y + 1)
        result += dfs(x, y - 1)
        result += dfs(x + 1, y)
        result += dfs(x - 1, y)
        return result

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y]:
                return dfs(x, y)
    return 0
