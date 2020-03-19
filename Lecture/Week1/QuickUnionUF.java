// Eager algorithem

public class QuickUnionUF{
    private int[] parent;
    private int count;

    public QuickUnionUF(int n){
        parent = new int[n];
        count = n;
        for (int i = 0, i<n; i++){
            parent[i] = i;
        }
    }

    public int count(){
        return count;
    }

    public int find(int p){

    }

    private void validate(int p){

    }
}