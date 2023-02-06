# dam design


def Soltion(wallPositions: list, wallHeights: list):
    wallPositions = []
    wallHeights = []

    n = wallPositions[-1]
    print(n)
    result = []

    for i in range(n - 1):
        if wallPositions[i + 1] - wallPositions[i] == 1:
            result.append(wallHeights[i])
        elif (wallPositions[i + 1] - wallPositions[i]) % 2 == 0:
            if wallHeights[i + 1] - wallHeights[i] > 1:
                return 0
            else:
                mid = (wallHeights[i + 1] + wallHeights[i]) / 2
                result.append(mid)

        elif (wallPositions[i + 1] - wallPositions[i]) % 2 == 1:
            if wallHeights[i + 1] - wallHeights[i] > 3:
                return 0
            else:
                mid = (wallHeights[i + 1] + wallHeights[i]) / 2
                result.append(mid + 1)
        else:
            return 0
