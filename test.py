def minMoves(n, startRow, startCol, endRow, endCol):
    # Write your code here
    def findNeighbors(node, matrix):
        index = [[-2, 1], [2, 1], [1, -2], [1, 2], [-2, -1], [2, -1], [-1, -2], [-1, 2]]
        curr_row = node[0]
        curr_column = node[1]
        neighbors = []
        for ele in index:
            new_row = curr_row + ele[0]
            new_column = curr_column + ele[1]
            if new_row >= 0 and new_row < matrix and new_column >= 0 and new_column < matrix:
                neighbors.append([new_row, new_column])

        return neighbors

    curr_row = startRow
    curr_column = startCol
    queue = [[[curr_row, curr_column]]]
    visited = set(str([curr_row, curr_column]))
    count = 0
    while queue:
        curr_level = queue.pop(0)
        # print(len(curr_level))
        new_level = []
        in_new_level = set()
        for node in curr_level:
            curr_node = node
            if curr_node[0] == endRow and curr_node[1] == endCol:
                return count
            visited.add(str(curr_node))

            neighbors = findNeighbors(curr_node, n)

            for ele in neighbors:
                if str(ele) not in visited and (str(ele) not in in_new_level) :
                    new_level.append(ele)
                    in_new_level.add(str(ele))
        queue.append(new_level)
        count += 1

    return -1


print(minMoves(30, 25, 2, 23, 29))
