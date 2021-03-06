from enum import Enum


class Status(Enum):
    X = 1
    O = 2
    NONE = 3
    DRAW = 4


BSIZE = 3


class XOBoard:
    def __init__(self):
        self.gameCharacters = ['X', 'O']
        self.sizeOfBoard = BSIZE * BSIZE
        self.gameMatrix = [[' ' for x in range(BSIZE)] for y in range(BSIZE)]
        self.fullCells = 0

    def Display(self):
        board = ""
        for i in range(BSIZE):
            if i == 0:
                board += self.RowOfEmptyColumns()

            for k in range(BSIZE):
                board += "  {}  ".format(self.gameMatrix[i][k])
                if k < BSIZE - 1:
                    board += "|"
            board += "\n"

            if i < BSIZE - 1:
                for m in range(BSIZE):
                    board += "-----"
                    if m < BSIZE - 1:
                        board += "|"
                board += "\n"

            if i == BSIZE - 1:
                board += self.RowOfEmptyColumns()
        print(board)

    def Put(self, character):
        correctInput = False

        while not correctInput:
            try:
                x, y = self.AskForInput(character)

                if self.gameMatrix[x][y] == ' ':
                    self.gameMatrix[x][y] = character
                    correctInput = True
                else:
                    print("Put your character on empty cell")

            except ValueError:
                print("Value Error.")
            except IndexError:
                print("Index Error.")
            except:
                print("Input Erorr.")
                correctInput = False

    def Status(self):
        retStatus = Status.NONE
        if self.fullCells >= 2 * BSIZE - 1:
            retStatus = self.CheckDiagonals()

            if retStatus == Status.NONE:
                retStatus = self.CheckColumnsAndRows()

            if retStatus == Status.NONE and self.fullCells == BSIZE * BSIZE:
                return Status.DRAW
        return retStatus

    def RowOfEmptyColumns(self):
        row = ""
        for j in range(BSIZE):
            row += "     "
            if j < BSIZE - 1:
                row += "|"
        row += "\n"
        return row

    def AskForInput(self, character):
        print("Put {} on the board".format(character))
        x, y = input("Where you would like to put your character(tap x,y coordinates)\n").split(",")
        return int(x), int(y)

    def CheckColumnsAndRows(self):
        for i in range(BSIZE):
            horizontal = self.gameMatrix[i][0]
            horizontalCnt = 0 if horizontal == ' ' else 1
            vertical = self.gameMatrix[0][i]
            verticalCnt = 0 if vertical == ' ' else 1
            for j in range(1, BSIZE):
                if horizontal != ' ' and self.gameMatrix[i][j] == horizontal:
                    horizontalCnt += 1
                if vertical != ' ' and self.gameMatrix[j][i] == vertical:
                    verticalCnt += 1
            if horizontalCnt == BSIZE:
                return Status.X if horizontal == 'X' else Status.O
            elif verticalCnt == BSIZE:
                return Status.X if vertical == 'X' else Status.O
        else:
            return Status.NONE

    def CheckDiagonals(self):
        lToR = self.gameMatrix[0][0]
        lToRCnt = 0 if lToR == ' ' else 1
        rToL = self.gameMatrix[0][BSIZE - 1]
        rToLCnt = 0 if rToL == ' ' else 1
        for i in range(1, BSIZE):
            if lToR != ' ' and self.gameMatrix[i][i] == lToR:
                lToRCnt += 1
            if rToL != ' ' and self.gameMatrix[i][BSIZE - 1 - i] == rToL:
                rToLCnt += 1
        if lToRCnt == BSIZE:
            return Status.X if lToR == 'X' else Status.O
        elif rToLCnt == BSIZE:
            return Status.X if rToL == 'X' else Status.O
        else:
            return Status.NONE
