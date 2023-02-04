public class Demo {

    public static void main(String[] args) {
        AbstractFactory sFactory = new RoundedShpaeFactory();
        Shape shape1 = sFactory.getShape("rectangle");
        shape1.draw();

        AbstractFactory sFactory2 = new ShapeFactory();
        Shape shape2 = sFactory2.getShape("rectangle");
        shape2.draw();
    }
    
}
