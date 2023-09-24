public class B_tree<T>{
    public int length;
    public Node<T> root;
    public B_tree(int length){
        this.length = length;
        this.root = new Node(length);
    }

    public void add(T element){
        root.add(element);
    }

    public T remove(T element){
        return root.remove(element);
    }

    public boolean search(T element){
        return root.search(element);
    }
}