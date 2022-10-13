import java.util.*;

//We need to import Adjacent class, Edge class and UFSet class
class Adjacent {
    protected int dest;
    protected double weight;
    protected Adjacent next;

    public Adjacent(int dest, double weight, Adjacent next){
	this.dest = dest;
	this.weight = weight;
	this.next = next;
    }
    
}

class Edge implements Comparable <Edge> {
    protected int beg;
    protected int dest;
    protected double weight;

    public Edge(int beg, int dest, double weight){
	this.beg = beg;
	this.dest = dest;
	this.weight = weight;
    }

    public int compareTo(Edge other){
	if (this.weight < other.weight) return -1;
	if (this.weight > other.weight) return 1;
	return 0;
    }

}

class Graph {
    Adjacent[] elArray;
    int numEdges;
    public Graph(int numVert) {
        this.elArray = new Adjacent[numVert];
        for(int i = 0; i < numVert; i++){
            elArray[i] = null;
        }
        numEdges = 0;
    }

    public boolean existEdge(int beg, int dest){
        Adjacent aux = this.elArray[beg];
        while(aux != null && aux.dest != dest) {
            aux = aux.next;
        }

        Adjacent aux2 = this.elArray[beg];
        while(aux2 != null && aux2.dest != dest) {
            aux2 = aux2.next;
        }

        return aux != null || aux2 != null;
    }

    public void addEdge(int beg, int dest, double weight){ 
        if(!existEdge(beg, dest)){
            Adjacent aux = this.elArray[beg];
            while(aux != null && aux.dest != dest){
                aux = aux.next;
            }
            if (aux != null) aux.weight = weight; //found -> We modify the weight
            else {//Not found -> We add it the first in the nodeList
                this.elArray[beg] = new Adjacent(dest, weight, this.elArray[beg]);
            }
            numEdges++;
        }
    }

    public void sumEdge(int num) {
        this.numEdges += num;
    }

}


public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        sc.nextLine(); //This next line doesn't read anything (Just the /n Character)
        while (cases-- > 0){
            String connection = sc.nextLine();
            List<String> edges = new ArrayList<String>();
            String[] vertex;
            while(!connection.contains("*")) {
                edges.add(connection);
                connection = sc.nextLine();
            }
            vertex = sc.nextLine().split(",");
            int numVert = vertex.length;

            Map<Character, Integer> cti = new HashMap<Character, Integer>();
            for(int i = 0; i < numVert; i++){
                cti.put(vertex[i].charAt(0), i);
            }
            int[] reached = new int[numVert];
            for (int i = 0; i < reached.length; i++){ //Initializing the array
                reached[i] = 0;
            }
            int tree = 0;
            int acorn = 0;

            if(edges.size() >= 1) {
                Map<Graph, List<Character>> mapa = new HashMap<Graph, List<Character>>(); 
                Graph gAux = new Graph(numVert);
                Character v1 = edges.get(0).charAt(1);
                Character v2 = edges.get(0).charAt(3);
                gAux.addEdge(cti.get(v1), cti.get(v2), 0);
                mapa.put(gAux, new ArrayList<Character>()); //We add the first element to avoid problems
                mapa.get(gAux).add(edges.get(0).charAt(1));
                mapa.get(gAux).add(edges.get(0).charAt(3));
                reached[cti.get(v1)] = 1;
                reached[cti.get(v2)] = 1;

                for(int i = 1; i < edges.size(); i++){
                    v1 = edges.get(i).charAt(1);
                    v2 = edges.get(i).charAt(3);
                    Graph p1 = find(v1, mapa);
                    Graph p2 = find(v2, mapa);
                    
                    if(p1 == null && p2 != null) { //we add v1 to p2
                        p2.addEdge(cti.get(v1), cti.get(v2), 0);
                        mapa.get(p2).add(v1);
                        reached[cti.get(v1)] = 1;
                        //System.out.println("Unido " + v1 + " a grafo de" + v2);

                    } else if(p1 != null && p2 == null) { //We add v2 to p1
                        p1.addEdge(cti.get(v1), cti.get(v2), 0);
                        mapa.get(p1).add(v2);
                        reached[cti.get(v2)] = 1;
                        //System.out.println("Unido " + v2 + " a grafo de" + v1);

                    } else if(p1 != null && p2 != null){ //We join the graphs
                        p1.addEdge(cti.get(v1), cti.get(v2), 0);
                        mapa.get(p1).addAll(mapa.get(p2));
                        p1.sumEdge(p2.numEdges);
                        //System.out.println("Unidos grafos, actuales: " + mapa.keySet().size());
                        mapa.remove(p2);
                    } else { //Both are null
                        gAux = new Graph(numVert);
                        gAux.addEdge(cti.get(v1), cti.get(v2), 0);
                        mapa.put(gAux, new ArrayList<Character>());
                        mapa.get(gAux).add(v1);
                        mapa.get(gAux).add(v2);
                        reached[cti.get(v1)] = 1;
                        reached[cti.get(v2)] = 1;
                        //System.out.println("Vreado nuevo grafo");
                    }

                    //System.out.println("Grafos restantes: " + mapa.keySet().size());

                }

                //System.out.println("numero de grafos = " + mapa.keySet().size());
                for(Graph g : mapa.keySet()){
                    if (g.numEdges == mapa.get(g).size() - 1) tree++;
                }
            }

            

            for(int i : reached){
                if (i == 0) acorn++;
            }

            System.out.println("There are " + tree + " tree(s) and " + acorn + " acorn(s).");


            
        }


    }


    public static Graph find(Character c, Map<Graph, List<Character>> m){
        Graph sol = null;
        for(Graph g : m.keySet()){
            if(m.get(g).contains(c)) {
                sol = g;
                break;
            }
        }
        //System.out.println("Tiene grafo " + c + "? " + sol != null);
        return sol;
    }
}