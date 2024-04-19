from Model.Graph import Graph
from View.displayGraph import displayGraph
from View.displayMenu import displayMenu
from Model.Helper import verifyCycle, hasNegativeEdges, computeRanks # calculateLatestDates

def main():

    displayMenu()

    """project_end_date = 50
        try:
            latest_dates = calculateLatestDates(graph, project_end_date)
            for vertex_value, start_date in latest_dates.items():
                print(f"Latest start time for task {vertex_value}: {start_date}")
            print("Les dates les plus tardives ont été calculées.")
        except ValueError as e:
            print(e)"""

if __name__ == "__main__":
    main()