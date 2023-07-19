public class Element<T extends Number | String> {
    private T value;

    public Element(T value){
        this.exists = true;
    }
    public Element(){
        this.value = null;
    }

    public void givevalue(T val){
        this.value = val;
    }
    public T getvalue(){
        return value;
    }

    public int compare(T other){
        if(this.value instanceof Number && other instanceof Number){
            if(value > other){
                return -1
            }
            if(value < other){
                return 1
            }
            return 0
        }
        if(this.value instanceof String && other instanceof String){
            return other.compareToIgnoreCase(this.value)
        }
        throw new IllegalArgumentException("Unsupported types for comparison.");
    }
}