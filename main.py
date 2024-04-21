from Model.Graph import Graph
from View.MainMenu import mainMenu
from Model.Helper import verifyCycle, hasNegativeEdges, computeRanks # calculateLatestDates
from View.Tools import clearConsole


def main():
    mainMenu()
    clearConsole()


if __name__ == "__main__":
    main()