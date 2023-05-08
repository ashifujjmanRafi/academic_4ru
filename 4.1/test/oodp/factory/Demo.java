public class Demo {

    public static void main(String[] args) {
        ShapeMaker sm = new ShapeMaker();

        Shape s1 = sm.getShape("Square");
        s1.message();

    }
}
