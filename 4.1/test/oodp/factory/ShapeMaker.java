public class ShapeMaker {

    public Shape getShape(String shape)
    {
        
        if(shape.equalsIgnoreCase("square")){
            return new Square();
        }
        else if(shape.equalsIgnoreCase("rectangle")){
            return new Rectangle();
        }

        return null;
    }
    
}
