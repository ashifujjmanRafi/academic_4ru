public class ShapeMaker{
    private Shape  rec ;
    private Shape sqr ;

    public ShapeMaker(){
        rec = new Rectangle();
        sqr = new Square();

    }

    public void drawSquare(){
        sqr.message();
    }
}