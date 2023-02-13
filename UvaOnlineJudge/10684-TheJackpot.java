import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while (cases > 0) {
            int[] bets = new int[cases];
            for (int i = 0; i < cases; i++) {
                bets[i] = sc.nextInt();
            }

            int money = 0, cur = 0;

            for (int i = 0; i < cases; i++) {
                cur = Math.max(cur + bets[i], bets[i]);
                money = Math.max(money, cur);

            }

            if (money > 0) {
                System.out.println("The maximum winning streak is " + money + ".");
            } else {
                System.out.println("Losing streak.");
            }

            // bw.flush();
            cases = sc.nextInt();
        }

        sc.close();

    }

}