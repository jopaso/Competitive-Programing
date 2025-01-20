import java.util.Scanner;
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        List<String> lines = new ArrayList<String>();
        while (sc.hasNextLine()){
            lines.add(sc.nextLine());
        }

        char[][] letters = new char[lines.size()][lines.get(0).length()];

        for (int i = 0; i < lines.size(); i++){
            letters[i] = lines.get(i).toCharArray();
        }

        int sizex = letters[0].length;
        int sizey = letters.length;

        int coincidencias = 0;

        for (int i = 0; i < letters.length; i++) {
            for (int j = 0; j < letters[i].length; j++){
                if (letters[i][j] == 'A') coincidencias += check_diagonal(i, j, letters, sizex, sizey);
            }
        }

        System.out.println("Conicidencias: " + coincidencias);

    }



    public static int check_diagonal(int i, int j, char[][] letters, int sizex, int sizey){
       if (i==0 || j==0 || i == sizey-1 || j == sizex-1) return 0;
       boolean diag1 = (letters[i-1][j-1] == 'M' && letters[i+1][j+1] == 'S') || (letters[i-1][j-1] == 'S' && letters[i+1][j+1] == 'M');  //Negative diagonal
       boolean diag2 = (letters[i-1][j+1] == 'M' && letters[i+1][j-1] == 'S') || (letters[i-1][j+1] == 'S' && letters[i+1][j-1] == 'M'); //positive diagonal

       if (diag1 && diag2) {
            System.out.println("Found X-MAS in: (" + i + ", " + j + ")");
            return 1;
       }

       return 0;
    }

}