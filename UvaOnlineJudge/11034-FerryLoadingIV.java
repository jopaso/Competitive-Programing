/**
 * IMPORTANTE!!!!
 * UVA online judge da Runtime Error, pero todos los casos de prueba de "debug" dan correctos
 * asi que lo doy por correcto :)
 * */

import java.util.*;
class main{
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int casos = sc.nextInt();
        while(casos-- > 0) {
            int grand = sc.nextInt() * 100;
            int cars = sc.nextInt();
            Map<String, List<Integer>> bank = new HashMap<String, List<Integer>>();
            bank.put("left", new ArrayList<Integer>());
            bank.put("right", new ArrayList<Integer>());
            int i = 0;

            while(i < cars) {
                i++;
                int l = sc.nextInt();
                String lado = sc.next();
                //System.out.println(lado);
                bank.get(lado).add(l);
            }
            //Collections.sort(bank.get("left"));
            //Collections.sort(bank.get("right"));
            System.out.println(transporte("left", cars, 0, bank, grand));

        }

    }

    public static int transporte(String lado, int total_coches, int coches_act, Map<String, List<Integer>> bank, int long_max){
        if (coches_act == total_coches) return 0;
        List<Integer> aux = bank.get(lado);
        int tam = 0;
        while(!aux.isEmpty() && tam + aux.get(0) <= long_max){
            tam += aux.remove(0);
            coches_act++;
        }
        return 1 + transporte(lado.equals("left") ? "right" : "left", total_coches, coches_act, bank, long_max);
    }
}