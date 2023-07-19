public class Node<T>{
    public Element<T>[] element_arr;
    public Node<T>[] children;
    private int id;
    private int index;
    public int length; 
    private static int staticindex = 0;
    public Node<T> parrent;

    public Node(int length,Node<T> parrent){
        this.element_arr = new Element[length];
        this.children = new Node[length + 1];
        this.parrent = parrent;
        this.id = staticindex++;
        this.length = length;
        for (int i = 0; i < length; i++) {
            if (this.element_arr[i] == null) {
                this.element_arr[i] = new Element<>();
            }
        }
    }

    public Node(int length, Node<T> parrent, Element<T>[] element_arr_2 , Node<T>[] children_2){
        this(length,parrent);
        if (element_arr_2.length > 0) {
            System.arraycopy(element_arr_2, 0, this.element_arr, 0, element_arr_2.length);
        }
        if (children_2.length > 0) {
            System.arraycopy(children_2, 0, this.children, 0, children_2.length);
        }

        for (int i = 0; i < length; i++) {
            if (this.element_arr[i] == null) {
                this.element_arr[i] = new Element<>();
            }
        }
    }

    public setindex(int ind){
        this.index = ind;
    }
    public getid(){
        return this.id;
    }
    public getidex(){
        return this.index;
    }

    protected void add(T element){
        Element newel = new Element(element);
        j = 0;
        while(j < length){
            j++;        }
    }

    protected T remove(T element){
        return element;
    }

}