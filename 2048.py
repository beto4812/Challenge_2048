import numpy
import random
import sys


def main():
    matrix = numpy.zeros([4, 4])

    for x in range(0, 4):  # Reads from input
        b = numpy.array(map(int, raw_input().split()))
        for j in range(0, len(b)):
            matrix[x][j] = b[j]

    moves = int(raw_input())

    moves_list = []

    for mvs in range(0, moves):
        moves_list.append(raw_input());

    for move in moves_list:  # For each move
        if move == "Izquierda":
            rotations = 0;
        elif move == "Arriba":
            rotations = 1;
        elif move == "Derecha":
            rotations = 2;
        elif move == "Abajo":
            rotations = 3;

        zeroes = set()  # All zeros are saved to put matrix random 2 efficiently
        matrix = numpy.rot90(matrix, rotations)  # The matrix is rotated to use the same code on each case

        for x in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[x][j] == 0:  # If 0 slides next encountered integer
                    zeroes.add((x, j))
                    for k in range(j, len(matrix[0])):
                        if k + 1 <= len(matrix[0]) and matrix[x][k] != 0:
                            matrix[x][j] = matrix[x][k]
                            zeroes.discard((x, j))
                            matrix[x][k] = 0
                            zeroes.add((x, k))
                            break

        for x in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if j + 1 < len(matrix[0]) and matrix[x][j] != 0 and matrix[x][j] != 2048 and matrix[x][j] == matrix[x][j + 1]:
                    # Not 0, check for contiguous and sum
                    matrix[x][j] = matrix[x][j] + matrix[x][j + 1]
                    matrix[x][j + 1] = 0
                    zeroes.add((x, j + 1))
                if j >= 1 and matrix[x][j] != 0 and matrix[x][j - 1] == 0:
                    matrix[x][j - 1] = matrix[x][j]
                    zeroes.discard((x, j - 1))
                    matrix[x][j] = 0
                    zeroes.add((x, j))

        if len(zeroes) >= 1:  # If possible spawn matrix random 2
            rand = random.randint(0, len(zeroes) - 1)
            zeroes_list = list(zeroes)
            matrix[zeroes_list[rand][0]][zeroes_list[rand][1]] = 2

        matrix = numpy.rot90(matrix, 4 - rotations)  # Matrix set to original state

    for x in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            sys.stdout.write(format(matrix[x][j], 'f').rstrip('0').replace(".", "")+"\t\t\t")
        print ""


if __name__ == "__main__":
    main()
