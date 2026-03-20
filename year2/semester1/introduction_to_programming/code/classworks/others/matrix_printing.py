import numpy as np


def main():
    matrix = [[5, 6, 7],
              [8, 9, 10]]

    transposed_matrix = np.array(matrix).T

    print("\n".join(f"row: {i}: {row[0]} {row[1]} {row[2]}" for i, row in enumerate(matrix)))
    print()
    print("\n".join(f"column: {i}: {column[0]} {column[1]}" for i, column in enumerate(transposed_matrix)))


if __name__ == "__main__":
    main()
