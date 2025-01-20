import sys


class Graph:
    def __init__(self, value):
        self.value = value
        self.queue = []
        self.visited = False
    
    def add_to_queue(self, graph):
        if graph != '.' and graph.value == self.value + 1:
            self.queue.append(graph)
            
    
    def __str__(self):
        return f"Graph value {self.value} and Queue {self.queue}"


def create_graphs(mapa):
    graph_mapa = []
    for eli in mapa: # Create all graphs
        graph_row = []
        for elj in eli:
            if not '.' == elj:
                graph_row.append(Graph(int(elj)))
            else:
                graph_row.append('.')
        graph_mapa.append(graph_row)

    graphs = []
    for i, row in enumerate(graph_mapa): # Create queues
        for j, act_graph in enumerate(row):
            if act_graph != '.':
            
                if i > 0:
                    act_graph.add_to_queue(graph_mapa[i-1][j])
                
                if i < len(graph_mapa)-1:
                        act_graph.add_to_queue(graph_mapa[i+1][j])
                
                if j > 0:
                    act_graph.add_to_queue(graph_mapa[i][j-1])
                
                if j < len(graph_mapa)-1:
                        act_graph.add_to_queue(graph_mapa[i][j+1])

                #print(act_graph)
                graphs.append(act_graph)

    return graphs
            

def search_trails(actual_graph):
    if actual_graph.value == 9:
        return 1
    
    else: #Search upper path
        queue = actual_graph.queue.copy()
        trails = 0
        while queue:
            popped = queue.pop()
            #print(f'Advancig to graph {popped} from {actual_graph} ')
            trails += search_trails(popped)
        return trails


def put_False(graphs):
    for g in graphs:
        g.visited = False
def main(mapa):
    graphs = create_graphs(mapa)

    score = 0
    for graph in graphs:
        if graph.value == 0:
            th_score = search_trails(graph)
            #put_False(graphs)
            score += th_score
            print(f'Score for TH {graph}: {th_score}') 

    print(f'\n\nSCORE: {score}')


if __name__ == '__main__':
    lines = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    mapa = []

    for line in lines:
        row = []
        for el in line.strip():
            row.append(el)
        mapa.append(row)

    main(mapa)  