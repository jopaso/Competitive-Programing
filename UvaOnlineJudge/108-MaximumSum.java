import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n;
        int[][] mat;

        while(sc.hasNextInt()) {
            n = sc.nextInt();
            mat = new int[n][n];
            //Fill the matrice
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    mat[i][j] = sc.nextInt();
                }
            }

            System.out.println(maxSubRectangle(mat, n));
        }

        sc.close();

    }

    public static int maxSubRectangle(int[][] mat, int n){
        int max = Integer.MIN_VALUE;
        int[] values;
        for(int left = 0; left < n; left++) {
            values = new int[n];
            for (int right = left; right < n; right++){
                for(int row = 0; row < n; row++){
                    if(right == left) values[row] = mat[row][right];
                    else values[row] += mat[row][right];

                    max = Math.max(max, values[row]);
                }

                max = Math.max(max, kadane(values, n));
            }
        }
        return max;
    }

    //Returns de largest consecutive sum of the array
    public static int kadane(int[] values, int n) {
        int max = Integer.MIN_VALUE;
        int current = 0;
        for(int i = 0; i < n; i++){
            current += values[i];
            if(current < 0) {
                current = 0;
                max = Math.max(max, values[i]);
            } else max = Math.max(max, current);
        }

        return max;
    }

}