class MovingAverage {
    Queue<Integer> queue;
    int sizeC;

    public MovingAverage(int size) {
        queue = new LinkedList<>();
         sizeC = size;
    }
    
    public double next(int val) {
        
        while (!queue.isEmpty() && queue.size() >= sizeC){
            queue.poll();
        }
        
        queue.offer(val);
        
        double count = 0;
        double ans = 0;
        
        for (int c: queue){
            count += c;
        }
        
        System.out.println(count);
        ans = count/ queue.size();
        
        return ans;
        
        
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */