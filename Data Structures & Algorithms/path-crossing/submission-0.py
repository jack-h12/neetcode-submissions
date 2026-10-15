class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points = set()
        points.add((0, 0))
        prev_pos = (0, 0)
        for i in range(len(path)):
            if path[i] == "N":
                prev_pos = (prev_pos[0], prev_pos[1] + 1)
                if prev_pos in points:
                    return True
                else:
                    points.add(prev_pos)
            elif path[i] == "S":
                prev_pos = (prev_pos[0], prev_pos[1] - 1)
                if prev_pos in points:
                    return True
                else:
                    points.add(prev_pos)
            elif path[i] == "W":
                prev_pos = (prev_pos[0] - 1, prev_pos[1])
                if prev_pos in points:
                    return True
                else:
                    points.add(prev_pos)
            elif path[i] == "E":
                prev_pos = (prev_pos[0] + 1, prev_pos[1])
                if prev_pos in points:
                    return True
                else:
                    points.add(prev_pos)
        return False
