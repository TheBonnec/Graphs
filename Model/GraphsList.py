from Model.Graph import Graph
from os import listdir
import re


def getAllGraphs():
    files: list[str] = listdir('GraphsFiles')
    graphsName: list[str] = []
    graphs: list[Graph] = []

    # Create graphs names based on file names
    for file in files:
        newGraphName = file
        newGraphName = newGraphName[0].upper() + newGraphName[1:]   # First letter in uppercase
        newGraphName = newGraphName[:5] + " " + newGraphName[5:]    # Space between 'Table' and the number
        newGraphName = newGraphName.split(".")[0]                   # remove the .txt
        graphsName.append(newGraphName)
    
    # Get all graphs
    for index in range(len(files)):
        newGraph = Graph(name = graphsName[index], fileName = f"GraphsFiles/{files[index]}")
        graphs.append(newGraph)
    
    sortGraphs(graphs = graphs)
    
    return graphs



def sortGraphs(graphs: list[Graph]):
    graphs.sort(key = lambda x: extractNumber(text = x.name), reverse = False)



def extractNumber(text: str) -> int:
    match = re.search(r'\d+', text)
    return int(match.group()) if match else None
