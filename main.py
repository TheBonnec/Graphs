from Model.Graph import Graph
from View.displayGraph import displayGraph
from View.displayMenu import displayMenu
from Model.Helper import has_negative_edges, calculate_latest_dates


def main():
    graph = Graph("graph1","GraphsFiles/table3.txt")
    try:
        if has_negative_edges(graph):
            print("Le graphe a des arêtes négatives.")
        else:
            print("Le graphe n'a pas d'arêtes négatives.")
            latest_dates = calculate_latest_dates(graph)   
            print("Les dates les plus tardives ont été calculées.")
    except ValueError as e:
        print(e)    
        
if __name__ == "__main__":
    main()