if __name__ == "__main__":
    size = 10
    default = []
    matMax = [[0] * size for i in range(size)]
    matMin = [[0] * size for j in range(size)]
    for i in range(size):
        default.append(list(map(int, input().split())))
        #заполнили изначальную матрицу

    matMax[0][0] = default[0][0]
    matMin[0][0] = default[0][0]

    for j in range(1, size):
        matMax[0][j] = matMax[0][j - 1] + default[0][j]
        matMin[0][j] = matMin[0][j - 1] + default[0][j]

    for i in range(1, size):
        matMax[i][0] = matMax[i - 1][0] + default[i][0]
        matMin[i][0] = matMin[i - 1][0] + default[i][0]
#заполнили по горизонтали и вертикали

    for i in range(1, size):
        for j in range(1, size):
            matMax[i][j] = max(matMax[i - 1][j], matMax[i][j - 1]) + default[i][j]
            matMin[i][j] = min(matMin[i - 1][j], matMin[i][j - 1]) + default[i][j]

    print(matMax[-1][-1], matMin[-1][-1])