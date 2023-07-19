public class B_tree<T extends Number | String>{
    public int length;
    public Node<T> root;
    public B_tree(int length){
        this.length = length;
        this.root = new Node(length , null)
    }

    public void add(T element){
        root.add(element)
    }
}