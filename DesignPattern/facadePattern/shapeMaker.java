
public class shapeMaker {
    private shape rectangle;
    private shape square;
    public shapeMaker(){
        rectangle = new rectangle();
        square = new square();
    }
    public void drawSquare(){
        square.draw();
    }
    public void drawRectangle(){
        rectangle.draw();
    }

}
