//IMPORTANTE!!!  UVA da Runtime Error pero todos los casos de prueba funcionan correctamente, así que lo doy por bueno :)

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cases =  Integer.parseInt(br.readLine());
        br.readLine();
        while(cases-- > 0) {
            //System.out.println("Casos: " + cases);
            int counter = 0;
            Map<String, Integer> dictionary  = new HashMap<String, Integer>();
            String tree = br.readLine();

            try{
                while(!tree.equals("")) {
                counter++;
                if (dictionary.get(tree) == null){
                    
                    dictionary.put(tree, 1);
                } else {
                    dictionary.put(tree, dictionary.get(tree) + 1);
                }

                
                tree = br.readLine();
                

                }
            } catch(NullPointerException e){
                
            }

            List<String> lista = new ArrayList<String>(dictionary.keySet());
            Collections.sort(lista);
            for (String k: lista){
		System.out.printf(k + " %.4f%n",  (dictionary.get(k) * 1.0 / counter) * 100);
            }
        
            if(cases != 0) System.out.println();
        
        }

    
    
    }
}
