public class Node<T>{
    public Element<T>[] element_arr;
    public Node<T>[] children;
    private int id;
    public int length; 
    private static int staticindex = 0;
    public Node(int length){
        this.id = staticindex;
        staticindex++;
        this.element_arr = new Element[length];
        this.children = new Node[length + 1];
    }

    public void add(T a){
        Element element = new Element<T>(a);

    }

    private void split(Element element, Node[] left_nodes, Element[] left_elelement, Node[] right_nodes, Element[] right_elements){

    }

    public void remove(T a){

    }

    public void search(T a){
        for(int i = 0; i < length; i++){
            
        }
    }
}