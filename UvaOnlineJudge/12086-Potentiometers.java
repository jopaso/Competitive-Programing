import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args){
  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        //PrintWriter out = new PrintWriter(System.out);
        int caso = 1;
        try{
            int nPotmeter = Integer.parseInt(br.readLine());
            while(nPotmeter != 0) {
                if(caso != 1) bw.write("\n");
                bw.write("Case " + caso++ + ":\n");
                bw.flush();
                int[] resistance = new int[nPotmeter];
                for (int i = 0; i < nPotmeter; i++){
                    resistance[i] = Integer.parseInt(br.readLine());
                }
                SegmentTree sg = new SegmentTree(resistance);
                StringTokenizer st = new StringTokenizer(br.readLine());
                String tok = st.nextToken();
                while(!tok.equals("END")){
                    if(tok.equals("S")) {
                        int i = Integer.parseInt(st.nextToken()) - 1;
                        sg.modify(i, Integer.parseInt(st.nextToken()));
                    }
                    else{
                        bw.write(sg.measure(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1) + "\n");
                    }
                    st = new StringTokenizer(br.readLine());
                    tok = st.nextToken();
                    bw.flush();
                }
                nPotmeter = Integer.parseInt(br.readLine());
                
            }
        }
        catch(IOException e) {}
    }
}

class Node{
    int start, end, val;
    public Node(int start, int end, int val){
        this.start = start;
        this.end = end;
        this.val = val;
    }
}
class SegmentTree{
    private int[] a;
    private int n;
    private int[] tree;
    public SegmentTree(int[] a) {
        this.a = a.clone();
        this.n = a.length;
        tree = new int[(n << 1) << 1];
        build(1, 0, this.n - 1); //We build the tree
    }

    private void build(int node, int start, int end) {
        if(start == end) tree[node] = a[start];
        else{
            
            int mid = (start + end) >> 1;
            int nodeL = node << 1;
            int nodeR = (node << 1) + 1;  
            build(nodeL, start, mid);
            build(nodeR, mid + 1, end);

            tree[node] = tree[nodeL] + tree[nodeR];
        }
    }

    public void modify(int i, int val){
        modify(1, 0, n - 1, i, val);
    }

    private void modify(int node, int start, int end, int i, int val){
        if(start == end && start == i) {
            tree[node] = val;
            a[i] = val;
        }
        else{
            int mid = (start + end) >> 1;
            int nodeL = node << 1;
            int nodeR = (node << 1) + 1;  
            if(i <= mid) modify(nodeL, start, mid, i, val);
            else modify(nodeR, mid + 1, end, i, val);

            tree[node] = tree[nodeL] + tree[nodeR];
        }
    }

    public int measure(int i, int j){
        return measure(1, 0, n - 1, i, j);
    }

    private int measure(int node, int start, int end, int i, int j){
        if(start > j || end < i) return 0;
        if(i <= start && end <= j) return tree[node];
        int mid = (start + end) >> 1;
        int nodeL = node << 1;
        int nodeR = (node << 1) + 1;  

        return  measure(nodeL, start, mid, i, j) + measure(nodeR, mid + 1, end, i, j);


    }
}