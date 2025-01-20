import java.io.*;
import java.util.List;
import java.util.*;
import java.util.Scanner;

public class Main{

    public static void main (String[] args){
        List<Robot> robots = read_input();
        //Object[][] hall = new Object[103][101];
        int maxX = 101;
        int maxY = 103;
        int times = 100;
        int[] quadrants = {0, 0, 0, 0};
        for (Robot r : robots){
            int q = r.move(times, maxX, maxY);
            if (q >= 0){
                quadrants[q]++;
            }
            System.out.println("Robot in (" + r.getPosX() + ", " + r.getPosY() + ") with vel: (" + r.getVelX() + ", " + r.getvelY() + ") and quadrant: " + q);

        }

        for (int q : quadrants) System.out.print(q + ", ");

        int safe_fact = 1;
        for (int i: quadrants) safe_fact *= i;

        System.out.println("Safety factor: " + safe_fact);
    }

    public static List<Robot> read_input(){
        Scanner sc = new Scanner(System.in);
        List<Robot> robots = new ArrayList<Robot>();
        while(sc.hasNextLine()){
            String[] arr = sc.nextLine().split(" ");
            String pos = arr[0].substring(2);
            String vel = arr[1].substring(2); 
            int posx = Integer.parseInt(pos.split(",")[0]);
            int posy = Integer.parseInt(pos.split(",")[1]);
            int velx = Integer.parseInt(vel.split(",")[0]);
            int vely = Integer.parseInt(vel.split(",")[1]);
            //System.out.println("Robot in (" + posx + ", " + posy + ") with vel: (" + velx + ", " + vely + ")");
            robots.add(new Robot(posx, posy, velx, vely));
        }

        return robots;
    }

}

class Robot{
    int posx, posy, velx, vely;
    public Robot(int posx,int posy,int velx,int vely){
        this.posx = posx;
        this.posy = posy;
        this.velx = velx;
        this.vely = vely;
    }

    public int getPosX(){
        return this.posx;
    }
    public int getPosY(){
        return this.posy;
    }

    public int getVelX(){
        return this.velx;
    }
    public int getvelY(){
        return this.vely;
    }

    public int move(int times, int maxX, int maxY){
        this.posx = ((this.posx + this.velx * times) % maxX + maxX) % maxX;
        //this.posy = (this.posy + this.vely * times % maxY) % maxY;
        //System.out.println(this.posy +  " + " + this.vely * times  + " = " + (((this.posy + this.vely * times) % maxY) + maxY));
        this.posy = (((this.posy + this.vely * times) % maxY) + maxY) % maxY;

        if (this.posx > maxX/2 && this.posy > maxY/2){
            return 3;
        } else if((this.posx > maxX/2 && this.posy < maxY/2)){
            return 2;
        } else if (this.posx < maxX/2 && this.posy > maxY/2){ return 1; 
        } else if (this.posx < maxX/2 && this.posy < maxY/2) return 0;
        else return -1; // Middle
    }
}