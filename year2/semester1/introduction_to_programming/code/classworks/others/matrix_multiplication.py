def row_by_row(default_matrix):
    return "\n".join(f"row: {i}: {row[0]} {row[1]} {row[2]}" for i, row in enumerate(default_matrix))


def multiplication(first_matrix, second_matrix):
    if len(first_matrix[0]) != len(second_matrix):
        raise ValueError("It's impossible - the matrix must have the same number of rows and columns")

    return (
        [sum(first_matrix[i][k] * second_matrix[k][j] for k in range(len(second_matrix)))
         for j in range(len(second_matrix[0]))]
        for i in range(len(first_matrix))
    )


def main():
    first_matrix = [[1, 2],
                    [3, 4]]

    second_matrix = [[5, 6, 7],
                     [8, 9, 10]]

    result = multiplication(first_matrix, second_matrix)
    print(row_by_row(result))


if __name__ == '__main__':
    main()
