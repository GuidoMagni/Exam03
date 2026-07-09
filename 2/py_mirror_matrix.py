def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for a in matrix:
        a.reverse()
    return matrix

print(mirror_matrix([[1,2,3],[4,5,6]]))