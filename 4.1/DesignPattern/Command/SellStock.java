public class SellStock implements Order{

    private Stock abStock;
    
    public SellStock(Stock abStock){
        this.abStock = abStock;
    }
    @Override public void execute(){
        abStock.sell();
    }
    
}
