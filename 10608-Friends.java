import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while (cases-- > 0){
            int people = sc.nextInt();
            int pairs = sc.nextInt();
            int pairs2 = pairs;
            int max = 1;
            //System.out.println("people = " + people + "   pairs = " + pairs);
            int[] array = new int[people]; 
            for(int i = 0; i < people; i++){
                array[i] = 0;
            }
            int numGroups = 1;
            Map<Integer, Integer> map = new HashMap<Integer, Integer>(); //Here we will store the number of people in each group
            while(pairs-- > 0){
                int p1 = sc.nextInt() - 1;
                int p2 = sc.nextInt() - 1;
                int l1 = array[p1];
                int l2 = array[p2];
                
                //System.out.println("L1: " + l1 + "       l2: " + l2);
                if(l1 == 0 && l2 != 0) { //we add p1 to l2
                    array[p1] = l2;
                    map.put(l2, map.get(l2) + 1);

                    //System.out.println(p1 + " añadido a grafo de " + p2);

                } else if(l1 != 0 && l2 == 0) { //We add p2 to l1
                    array[p2] = l1;
                    map.put(l1, map.get(l1) + 1);


                    //System.out.println(p2 + " añadido a grafo de " + p1);
                } else if(l1 == 0 && l2 == 0){ //Both are null
                    l1 = numGroups; //We will need it to modify the max
                    array[p2] = numGroups;
                    array[p1] = numGroups;
                    map.put(numGroups++, 2);
                    //System.out.println("Creado nuevo grafo para " + p1 + " y " + p2);
                } else if(l1 != l2){ //both have a graph and if they are different we join them
                    for(int i = 0; i < people; i++){
                        if(array[i] == l2) {
                            array[i] = l1;
                        }
                    }
                    map.put(l1, map.get(l1) + map.get(l2));
                    map.remove(l2);
                    //System.out.println("Unidos grafos de " + p1 + " y " + p2);
                    
                } 
                if(map.get(l1) != null && map.get(l1) > max) max = map.get(l1);
                if(map.get(l2) != null && map.get(l2) > max) max = map.get(l2);

            }


            System.out.println(max);
        
        }

    }

}
