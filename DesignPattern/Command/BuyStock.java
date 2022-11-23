public class BuyStock implements Order {
    private Stock abcstock;
    public BuyStock(Stock aStock){
        this.abcstock = aStock;
    }
    @Override public void execute(){
        abcstock.buy();
    }
    
}
