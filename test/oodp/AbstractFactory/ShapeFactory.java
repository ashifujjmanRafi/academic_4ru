public class ShapeFactory  extends AbstractFactory {

    @Override
    public Shape getShape(String shape) {
        if(shape.equalsIgnoreCase("SQUARE")) {
            return new Square();
        } else if (shape.equalsIgnoreCase("RECTANGLE")) {
            return new Rectangle();
        }
        return null;
    }


}
