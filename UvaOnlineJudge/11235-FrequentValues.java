import java.util.*;

import org.w3c.dom.traversal.NodeIterator;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        while(num != 0) { //The last line will contain a single 0
            int querys = sc.nextInt();
            //System.out.println("Number of querys: " + querys);
            int[] numbers = new int[num];
            for (int i = 0; i < num; i++){
                numbers[i] = sc.nextInt();
            }

            SegmentTree tree = new SegmentTree(numbers);
            while(querys-- > 0)
            {
                int i = sc.nextInt() - 1; //It's given starting by 1, so its needed to substract 1
                int j = sc.nextInt() - 1;
                //System.out.println("Computing query: i= " + i + " j = " + j);
                System.out.println(tree.query(i, j).max);
            }
               
            
            num = sc.nextInt();
        }
        sc.close();
    }

    static class Node{
        int maxLeft, maxRight, maxMid, max;
        public Node(int l, int r, int mid, int max) {
            this.maxLeft = l;
            this.maxRight = r;
            this.maxMid = mid;
            this.max = max;
        }
    }
    
    static class SegmentTree{
        Node[] tree;
        int[] num; //We will store here the n integers array
        int n; //length of the array

        public SegmentTree(int[] arr){
            num = arr.clone();
            n = num.length;
            tree = new Node[(n << 1) << 1]; //n * 4
            build(1, 0, n - 1);
        }

        void build(int node, int start, int end){
            if(start == end) {
                tree[node] = new Node(1, 1, 1, 1);
            } else {
                int mid = (start + end) >> 1;

                //create recursively the tree branches
                build(left(node), start, mid);
                build(right(node), mid + 1, end);

                Node nodeRight = tree[right(node)];
                Node nodeLeft = tree[left(node)];

                //compute the max values:
                int left, maxMid, right;
                if(num[start] == num[mid + 1]){left = nodeLeft.maxLeft + nodeRight.maxLeft; }
                else{ left = nodeLeft.maxLeft; }

                if(num[mid] == num[end]) { right = nodeLeft.maxRight + nodeRight.maxRight; }
                else {right = nodeRight.maxRight; }

                if(num[mid] == num[mid + 1]){ maxMid = nodeLeft.maxRight + nodeRight.maxLeft; }
                else{ maxMid = Math.max(nodeLeft.maxRight, nodeRight.maxLeft); }
            
                tree[node] = new Node(left, right, maxMid, Math.max(left, Math.max(right, Math.max(maxMid, Math.max(nodeLeft.max, nodeRight.max)))));
            }
        }

        Node query(int i, int j) {
            return query(1, 0, n - 1, i, j);
        }

        Node query(int node, int start, int end, int i, int j){
            if(start > j || end < i) return new Node(0, 0, 0, 0);
            if(start >= i && end <= j) return tree[node];

            int mid = (start + end) >> 1;
            Node nodeLeft = query(left(node), start, mid, i, j);
            Node nodeRight = query(right(node), mid + 1, end, i ,j);

            //compute the max values:
            int left, maxMid, right;
            if(num[start] == num[mid + 1]){ left = nodeLeft.maxLeft + nodeRight.maxLeft; }
            else{ left = nodeLeft.maxLeft; }

            if(num[mid] == num[end]) { right = nodeLeft.maxRight + nodeRight.maxRight; }
            else {right = nodeRight.maxRight; }

            if(num[mid] == num[mid + 1]){ maxMid = nodeLeft.maxRight + nodeRight.maxLeft; }
            else{ maxMid = Math.max(nodeLeft.maxRight, nodeRight.maxLeft); }
        
            return new Node(left, right, maxMid, Math.max(left, Math.max(right, Math.max(maxMid, Math.max(nodeLeft.max, nodeRight.max)))));
        
        }


        int left(int node) {return node << 1;}
        int right(int node) {return (node << 1) + 1;}
    }
}
