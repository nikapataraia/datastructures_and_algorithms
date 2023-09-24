public class Element<T> {
    private T value;

    public Element(T value){
        this.value = value;
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

    public int compare(T other) {
        if (value instanceof Number && other instanceof Number) {
            Number thisNumber = (Number) value;
            Number otherNumber = (Number) other;
            return Double.compare(thisNumber.doubleValue(), otherNumber.doubleValue());
        } else if (value instanceof String && other instanceof String) {
            String thisString = (String) value;
            return thisString.compareToIgnoreCase((String) other);
        } else {
            throw new IllegalArgumentException("Unsupported types for comparison.");
        }
    }
}