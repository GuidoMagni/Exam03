def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for a in matrix:
        a.reverse()
    return matrix