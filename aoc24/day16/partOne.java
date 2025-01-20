import java.security.KeyStore.Entry;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<ArrayList<Character>> maze = new ArrayList<ArrayList<Character>>();
        int startX = -1;
        int startY = -1;
        int endX = -1;
        int endY = -1;
        int counter = 0;
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            ArrayList<Character> row = new ArrayList<Character>();
            char[] c = line.toCharArray();
            for (int i = 0; i < c.length; i++) {
                row.add(c[i]);
                if (c[i] == 'E') {// end
                    endX = counter;
                    endY = i;
                } else if (c[i] == 'S') {// start
                    startX = counter;
                    startY = i;
                }

            }
            maze.add(row);
            counter++;
        }

        System.out.println("Starting point: " + startX + ", " + startY);
        System.out.println("Ending point: " + endX + ", " + endY);

        HashMap<Integer, HashMap<Integer, Node>> graph = getGraphs(maze);
        Node endingNode = graph.get(endX).get(endY);
        Node startNode = graph.get(startX).get(startY);
        startNode.min_value = 0;

        int direction = 1; // 1-> East 2-> North 3->South 4-> West

        start_algorithm(startNode, endingNode, direction);

        System.out.println("Minimum value: " + graph.get(endX).get(endY).min_value);

    }

    public static void start_algorithm(Node startingNode, Node endingNode, int direction) {
        //System.out.println(startingNode.toString());
        if (startingNode == endingNode){
            System.out.println("End node FOUND");
            return;
        }
        else {
            //System.out.println("Going " + direction + " From (" + startingNode.posX + ", " + startingNode.posY + ") with value " + startingNode.min_value);

            List<Pair> close_nodes = startingNode.get_nextNodes(direction);
            Collections.sort(close_nodes);

            for (Pair p : close_nodes) {

                start_algorithm(p.getNode(), endingNode, p.getDirection());


                }
            }
    }

    public static HashMap<Integer, HashMap<Integer, Node>> getGraphs(ArrayList<ArrayList<Character>> maze) {
        HashMap<Integer, HashMap<Integer, Node>> graph_pos = new HashMap<Integer, HashMap<Integer, Node>>();
        // ArrayList<Node> graph = new ArrayList<Node>();
        for (int i = 0; i < maze.size(); i++) {
            HashMap<Integer, Node> row_map = new HashMap<Integer, Node>();
            for (int j = 0; j < maze.get(i).size(); j++) {
                if (maze.get(i).get(j) != '#') {
                    Node n = new Node(-1, i, j);
                    row_map.put(j, n);
                    // graph.add(n);
                }

            }
            graph_pos.put(i, row_map);
        }

        Set<Integer> graph_keys = graph_pos.keySet();
        for (int i : graph_keys) {
            Set<Integer> row_keys = graph_pos.get(i).keySet();
            for (int j : row_keys) {
                Node n = graph_pos.get(i).get(j);

                // Add connected nodes
                if (graph_pos.containsKey(i - 1) && graph_pos.get(i - 1).containsKey(j)) {
                    n.insert_north(graph_pos.get(i - 1).get(j));
                }
                if (graph_pos.containsKey(i + 1) && graph_pos.get(i + 1).containsKey(j)) {
                    n.insert_south(graph_pos.get(i + 1).get(j));
                }
                if (graph_pos.containsKey(i) && graph_pos.get(i).containsKey(j - 1)) {
                    n.insert_west(graph_pos.get(i).get(j - 1));
                }
                if (graph_pos.containsKey(i) && graph_pos.get(i).containsKey(j + 1)) {
                    n.insert_east(graph_pos.get(i).get(j + 1));
                }
            }
        }

        return graph_pos;
    }
}

class Node {
    Node east;
    Node north;
    Node south;
    Node west;
    int min_value;
    int posX;
    int posY;

    public Node(int min_value, int posX, int posY) {
        this.min_value = min_value;
        this.posX = posX;
        this.posY = posY;
    }

    public void insert_east(Node east) {
        this.east = east;
    }

    public void insert_north(Node north) {
        this.north = north;
    }

    public void insert_south(Node south) {
        this.south = south;
    }

    public void insert_west(Node west) {
        this.west = west;
    }

    public ArrayList<Pair> get_nextNodes(int direction) {
        ArrayList<Pair> res = new ArrayList<Pair>();
        boolean is_lower = (east != null);
        is_lower = is_lower && (east.min_value < 0 || 
            (east.min_value > this.min_value + (direction - 1  == 0 ? 1 : 1001) || (east.east != null)));

        if (east != null && (east.min_value < 0 || 
                (east.min_value > this.min_value + (direction - 1  == 0 ? 1 : 1001) || (east.east != null && east.east.min_value > 0 && 
                                                east.east.min_value > this.min_value + (direction - 1  == 0 ? 1 : 1001) + 1)))) {
            east.min_value = this.min_value + (direction - 1  == 0 ? 1 : 1001);
            res.add(new Pair(east, 1));
        }

        if (north != null && (north.min_value < 0 || (north.min_value > this.min_value + (direction - 2  == 0 ? 1 : 1001) || (north.north != null && north.north.min_value > 0 && 
        north.north.min_value > this.min_value + (direction - 2  == 0 ? 1 : 1001) + 1)))) {
            north.min_value = this.min_value + (direction - 2  == 0 ? 1 : 1001);
            res.add(new Pair(north, 2));
        }

        if (south != null && (south.min_value < 0 || (south.min_value > this.min_value + (direction - 3  == 0 ? 1 : 1001) || (south.south != null && south.south.min_value > 0 && 
        south.south.min_value > this.min_value + (direction - 3  == 0 ? 1 : 1001) + 1)))) {
            south.min_value = this.min_value + (direction - 3  == 0 ? 1 : 1001);
            res.add(new Pair(south, 3));
        }
        
        if (west != null && (west.min_value < 0 || (west.min_value > this.min_value + (direction - 4  == 0 ? 1 : 1001) || (west.west != null && west.west.min_value > 0 && 
        west.west.min_value > this.min_value + (direction - 4  == 0 ? 1 : 1001) + 1)))) {
            west.min_value = this.min_value + (direction - 4  == 0 ? 1 : 1001);
            res.add(new Pair(west, 4));
        }


        // System.out.println("East: " + east + ", North: " + north + ", South " + south
        // + ", West " + west);

        // System.out.println("Returned length: " + res.size());
        Collections.sort(res);
        return res;

    }

    public String toString() {
        return "Node in position (" + this.posX + ", " + this.posY + ") min_value -> " + min_value;
    }
}

class Pair implements Comparable<Pair> {

    private final Node node;
    private final int direction;

    public Pair(Node node, int direction) {
        this.node = node;
        this.direction = direction;
    }

    public Node getNode() {
        return this.node;
    }

    public int getDirection() {
        return this.direction;
    }

    @Override
    public int compareTo(Pair other) {
        return this.node.min_value - other.node.min_value;
    }

    @Override
    public boolean equals(Object other) {
        Pair o = (Pair) other;
        return this.node == o.getNode();
    }

    public String toString() {
        return "Node min_val: " + this.node.min_value + " Direction: " + direction;
    }

}
