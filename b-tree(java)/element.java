public class Element<T> {
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

    public int compare(Element<T> other) {
        if (value instanceof Number && other.value instanceof Number) {
            Number thisNumber = (Number) value;
            Number otherNumber = (Number) other.value;
            return Double.compare(thisNumber.doubleValue(), otherNumber.doubleValue());
        } else if (value instanceof String && other.value instanceof String) {
            String thisString = (String) value;
            return thisString.compareToIgnoreCase((String) other.value);
        } else {
            throw new IllegalArgumentException("Unsupported types for comparison.");
        }
    }
}