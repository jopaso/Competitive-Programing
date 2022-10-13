import java.util.*;
class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()){
            int cases = sc.nextInt();
            //System.out.println("cases = " + cases);
            Stack<Integer> stack = new Stack<Integer>();
            Queue<Integer> queue = new LinkedList<Integer>();
            PriorityQueue<Integer> priority = new PriorityQueue<Integer>(Collections.reverseOrder());
            boolean isStack = true;
            boolean isQueue = true;
            boolean isPrioQ = true;
            while(cases-- > 0){
                int action = sc.nextInt();
                int element = sc.nextInt();
                if (action == 1) {
                    stack.push(element);
                    queue.add(element);
                    priority.add(element);
                    //System.out.println("Stack = " + stack + "\nQueue = " + queue + "\nPriority queue = " + priority + "\n*****************************************");
                } else { //It is compared if the result is similar
                    isStack = isStack && (stack.isEmpty() ? false : stack.pop() == element);
                    isQueue = isQueue && (queue.isEmpty() ? false : queue.remove() == element);
                    isPrioQ = isPrioQ && (priority.isEmpty() ? false : priority.remove() == element);
                }

            }

            if(isStack && !isQueue && !isPrioQ ) System.out.println("stack");
            else if(!isStack && isQueue && !isPrioQ ) System.out.println("queue");
            else if(!isStack && !isQueue && isPrioQ ) System.out.println("priority queue");
            else if(!isStack && !isQueue && !isPrioQ ) System.out.println("impossible");
            else { 
                System.out.println("not sure");
                //System.out.println("Stack --> " + isStack + "\nQueue --> " + isQueue + "\nPriority queue --> " + isPrioQ);
            }
            //System.out.println("--------------------------------");
        }

    }

}