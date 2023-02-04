public class RoundedShpaeFactory extends AbstractFactory {

    @Override
    public Shape getShape(String shapeType) {
        if (shapeType.equalsIgnoreCase("RECTANGLE")) {
            return new RoundedRec();
        } else if (shapeType.equalsIgnoreCase("SQUARE")) {
            return new RoundefSquare();
        }
        return null;
    }

}
