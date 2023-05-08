public class FactoryProducer {
    public static AbstractFactory getFactory(String factoryType) {
        if (factoryType.equalsIgnoreCase("RegularShape")) {
            return new ShapeFactory();
        } else if (factoryType.equalsIgnoreCase("RoundedShape")) {
            return new RoundedShapeFactory();
        }
        return null;
    }
}
