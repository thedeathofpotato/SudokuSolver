import cell

class Board:
    def __init__(self):
        self._cellsList = []
        for _ in range(9):
            row = []
            for _ in range(9):
                row.append(cell.Cell())
            self._cellsList.append(row)

        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if(not k == j):
                        self._cellsList[i][j].setConnected(self._cellsList[i][k])
                for l in range(9):
                    if(not l == i):
                        self._cellsList[i][j].setConnected(self._cellsList[l][j])
    