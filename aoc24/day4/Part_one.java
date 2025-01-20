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
            for (int j = 0; j < letters.length; j++){
                coincidencias += check_diagonal(i, j, letters, sizex, sizey) + check_vertical(i, j, letters, sizex, sizey) + check_horizontal(i, j, letters, sizex, sizey);
            }
        }

        System.out.println("Conicidencias: " + coincidencias);

    }

    public static int check_horizontal(int i, int j, char[][] letters, int sizex, int sizey){
        return check_horizontal_back(i, j, letters, sizex, sizey) + check_horizontal_front(i, j, letters, sizex, sizey);
    }

    private static int check_horizontal_back(int i, int j, char[][] letters, int sizex, int sizey){
        if (j < 3) return 0;

        String word = "" + letters[i][j] + letters[i][j-1] + letters[i][j-2] + letters[i][j-3]; 
        if (word.equals("XMAS")) System.out.println("Found horizontal back in: (" + i + ", " + j + ")");
        return word.equals("XMAS") ? 1 : 0;
    }
    private static int check_horizontal_front(int i, int j, char[][] letters, int sizex, int sizey){
        if (j + 3 >= sizex) return 0;

        String word = "" + letters[i][j] + letters[i][j+1] + letters[i][j+2] + letters[i][j+3]; 
        if (word.equals("XMAS")) System.out.println("Found horizontal front in: (" + i + ", " + j + ")");
        return word.equals("XMAS") ? 1 : 0;
    }

    public static int check_vertical(int i, int j, char[][] letters, int sizex, int sizey){
        return check_vertical_down(i, j, letters, sizex, sizey) + check_vertical_up(i, j, letters, sizex, sizey);
    }

    private static int check_vertical_up(int i, int j, char[][] letters, int sizex, int sizey){
        if (i < 3) return 0;

        String word = "" + letters[i][j] + letters[i-1][j] + letters[i-2][j] + letters[i-3][j]; 
        if (word.equals("XMAS")) System.out.println("Found vertical up in: (" + i + ", " + j + ")");
        return word.equals("XMAS") ? 1 : 0;
    }
    private static int check_vertical_down(int i, int j, char[][] letters, int sizex, int sizey){
        if (i + 3 >= sizey) return 0;

        String word = "" + letters[i][j] + letters[i+1][j] + letters[i+2][j] + letters[i+3][j]; 
        if (word.equals("XMAS")) System.out.println("Found vertical down in: (" + i + ", " + j + ")");
        return word.equals("XMAS") ? 1 : 0;
    }

    public static int check_diagonal(int i, int j, char[][] letters, int sizex, int sizey){
        return check_diagonal_up_back(i, j, letters, sizex, sizey) + check_diagonal_up_front(i, j, letters, sizex, sizey) + 
            check_diagonal_down_back(i, j, letters, sizex, sizey) + check_diagonal_down_front(i, j, letters, sizex, sizey);
    }

    private static int check_diagonal_up_back(int i, int j, char[][] letters, int sizex, int sizey){
        if (i < 3 || j < 3) return 0;
        String word = "" + letters[i][j] + letters[i-1][j-1] + letters[i-2][j-2] + letters[i-3][j-3];
        if (word.equals("XMAS")) System.out.println("Found diagonal up back in: (" + i + ", " + j + ")");
        return word.equals("XMAS") ? 1 : 0;
    }
    private static int check_diagonal_up_front(int i, int j, char[][] letters, int sizex, int sizey){
        if (i < 3 || j + 3 >= sizex) return 0;
        String word = "" + letters[i][j] + letters[i-1][j+1] + letters[i-2][j+2] + letters[i-3][j+3];
        if (word.equals("XMAS")) System.out.println("Found diagonal up front in: (" + i + ", " + j + ")");
        return word.equals("XMAS") ? 1 : 0;
    }
    private static int check_diagonal_down_back(int i, int j, char[][] letters, int sizex, int sizey){
        if (i + 3 >= sizey || j < 3) return 0;
        String word = "" + letters[i][j] + letters[i+1][j-1] + letters[i+2][j-2] + letters[i+3][j-3];
        if (word.equals("XMAS")) System.out.println("Found diagonal down back in: (" + i + ", " + j + ")");
        return word.equals("XMAS") ? 1 : 0;
    }
    private static int check_diagonal_down_front(int i, int j, char[][] letters, int sizex, int sizey){
        if (i + 3 >= sizey || j + 3 >= sizex) return 0;
        String word = "" + letters[i][j] + letters[i+1][j+1] + letters[i+2][j+2] + letters[i+3][j+3];
        if (word.equals("XMAS")) System.out.println("Found diagonal down front in: (" + i + ", " + j + ")");
        return word.equals("XMAS") ? 1 : 0;
    }

}