/******************************************************************************
 *  Compilation:  javac QuickFindUF.java
 *  Execution:  java QuickFindUF < input.txt
 *  Dependencies: StdIn.java StdOut.java
 *  Data files:   https://algs4.cs.princeton.edu/15uf/tinyUF.txt
 *                https://algs4.cs.princeton.edu/15uf/mediumUF.txt
 *                https://algs4.cs.princeton.edu/15uf/largeUF.txt
 *
 *  Quick-find algorithm.
 *
 ******************************************************************************/

public class QuickFindUF{
    private int[] id; // id[i] = component identifier of i
    private int count; // number of components
    
    public QuickFindUF(int N){ // Initialize data 
        id = new int[N];
        for(int i=0; i<N; i++){
            id[i] = i;
        }
    }

    public boolean connected(int p, int q){
        return id[p] == id[q];
    }
    // validate that p is a valid index 
    private void validate(int p){
        int n = id.length;
        if(p<0 || p >= n){
            throw new IllegalArgumentException("index " + p + " is not between 0 and "+ (n-1));
        }
    }

    public void union(int p, int q){
        int pid = id[p];
        int qid = id[q];

        for(int i = 0; i< id.length; i++){
            if(id[i] == pid){
                id[i] = qid;
        }
    }
}